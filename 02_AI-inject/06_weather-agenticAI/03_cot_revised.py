from openai import InternalServerError
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import time


load_dotenv()
import os


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The Weather in {city.title()} is: {response.text}"
    return "Sorry, I couldn't fetch the weather information."


def run_command(command: str):
    result = os.system(command)
    return result


available_tools = {"get_weather": get_weather, "run_command": run_command}


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# Initialize OpenAI client for Gemini API

SYSTEM_PROMPT = """
You are an expert AI assistant in resolving user queries using chain of thoughts.
You work on START, PLAN and OUTPUT steps.
You need to first plan the answer. The plan can be of multiple steps.
Once you think enough plan has done, finally you can give the final output.
you can also call a tool if required from the list of tools_available.

Rules:
- Always think step by step.
- Strictly follow the JSON format for the final output.
- Only run one step at one time
- the sequence is to start, plan and then output.

Output format :
{
    "step": "START" | "PLAN" | "OUTPUT" | "TOOL_CALL",
    "content": "string"
    "tool": "tool_name",         # only for TOOL_CALL step
    "input": "tool_input"        # only for TOOL_CALL step
}

Tools_available:    
- get_weather(city:str) : Takes city name as input Fetches the current weather information for the specified city.
- run_command(command:str) : Takes a command as input and runs it on the system shell, returning the result.

Example 1:

Question: How do I calculate the 2 + 3 * 5 / 10 ?
Answer: 
{ "step": "START", "content": "Hey, Can you solve 2 + 3 * 5 / 10" }
{ "step": "PLAN", "content": "Seems like user is interested in math problem" }
{ "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
{ "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
{ "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
{ "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
{ "step": "PLAN", "content": "We must perform divide that is 15 / 10  = 1.5" }
{ "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
{ "step": "PLAN", "content": "Now finally lets perform the add 3.5" }
{ "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans" }
{ "step": "OUTPUT", "content": "3.5" }

    
Example 2:

Question: What is the weather of lahore in pakistan ?
Answer: {
    START: Seems like user is interested in weather of lahore
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in weather information" }
    PLAN: { "step": "PLAN": "content": "Let's see is there any tool available to get the weather information" }
    PLAN: { "step": "PLAN": "content": "Yes, we have a tool called get_weather that can fetch the current weather information for a specified city." }
    PLAN: { "step": "PLAN": "content": "I need to call that tool to get the weather of lahore city" }
    PLAN: { "step": "TOOL": "tool" : "get_weather" : "input": "lahore" }
    PLAN: { "step": "OBSERVE": "tool": "get_weather", "output": "The temp of lahore is cloudy with 20 C" }
    PLAN: { "step": "PLAN": "content": "Great, we have fetched the weather information of lahore city" }
    OUTPUT: { "step": "OUTPUT": "content": "The current weather in lahore is 20 C with some cloudy sky." }


"""

print("\n")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }
]

while True:

    user_query = input("Query : ")

    message_history.append(
        {
            "role": "user",
            "content": user_query,
        }
    )

    print("Solving....")

    while True:

        # for i in range(3):
        #     try:
        #         response = client.chat.completions.create(
        #             model="gemini-robotics-er-1.5-preview",
        #             response_format={"type": "json_object"},
        #             messages=message_history,
        #         )
        #         break
        #     except InternalServerError:
        #         print("Model overloaded, retrying...")
        #         time.sleep(2)

        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=message_history,
        )

        raw_result = response.choices[0].message.content
        # Extract response content from API

        message_history.append({"role": "assistant", "content": raw_result})
        # Add AI response to history

        json_objects = []
        # Initialize list for parsed JSON objects

        lines = raw_result.strip().split("\n")
        # Split response into individual lines

        for line in lines:
            if line.strip():
                try:
                    obj = json.loads(line)
                    json_objects.append(obj)
                except json.JSONDecodeError:
                    pass

        for parsed_result in json_objects:

            if parsed_result.get("step") == "START":
                print("Starting...: ", parsed_result.get("content"))
                continue

            if parsed_result.get("step") == "TOOL":
                tool_name = parsed_result.get("tool")
                tool_input = parsed_result.get("input")
                print(f"Calling Tool: {tool_name} with input: {tool_input}")

                tool_response = available_tools[tool_name](tool_input)
                print(f"Tool Response: {tool_response}")

                message_history.append(
                    {
                        "role": "developer",
                        "content": json.dumps(
                            {
                                "step": "OBSERVE",
                                "tool": tool_name,
                                "input": tool_input,
                                "output": tool_response,
                            }
                        ),
                    }
                )
                continue

            if parsed_result.get("step") == "PLAN":
                print("Planning...: ", parsed_result.get("content"))
                continue

            if parsed_result.get("step") == "OUTPUT":
                print("Output = ", parsed_result.get("content"))
                break

        if json_objects and json_objects[-1].get("step") == "OUTPUT":
            break

    print("\n\n\n")
