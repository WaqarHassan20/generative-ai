from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
import os

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

Rules:
- Always think step by step.
- Strictly follow the JSON format for the final output.
- Only run one step at one time
- the sequence is to start, plan and then output.

Output format :
{
    "step": "START" | "PLAN" | "OUTPUT",
    "content": "string"
}

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
"""
# Chain-of-thought instructions: START -> PLAN (multiple steps) -> OUTPUT

print("\n\n\n")
# Add visual spacing

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }
]
# Initialize conversation history with system prompt

user_query = input("Query : ")
# Get user input

message_history.append(
    {
        "role": "user",
        "content": user_query,
    }
)
# Add user query to history

# Example: can you solve the 2 + 3 * 10 / 2

print("Solving....")
# Display processing status

while True:
    response = client.chat.completions.create(
        # model="gemini-2.0-flash",
        model="gemini-robotics-er-1.5-preview",
        response_format={"type": "json_object"},
        messages=message_history,
    )
    # Send request to Gemini API with full conversation history

    raw_result = response.choices[0].message.content
    # Extract response content from API
    
    message_history.append({"role": "assistant", "content": raw_result})
    # Add AI response to history
    
    json_objects = []
    # Initialize list for parsed JSON objects
    
    lines = raw_result.strip().split('\n')
    # Split response into individual lines
    
    for line in lines:
        if line.strip():
            try:
                obj = json.loads(line)
                json_objects.append(obj)
            except json.JSONDecodeError:
                pass
    # Parse each line as JSON
    
    for parsed_result in json_objects:
        # Process each JSON step
        
        if parsed_result.get("step") == "START":
            print("Starting...: ", parsed_result.get("content"))
            continue
        # Handle START step
        
        if parsed_result.get("step") == "PLAN":
            print("Planning...: ", parsed_result.get("content"))
            continue
        # Handle PLAN step

        if parsed_result.get("step") == "OUTPUT":
            print("Output = ", parsed_result.get("content"))
            break
        # Handle OUTPUT step (final answer)
    
    if json_objects and json_objects[-1].get("step") == "OUTPUT":
        break
    # Exit loop when OUTPUT received

print("\n\n\n")
# Add final spacing
