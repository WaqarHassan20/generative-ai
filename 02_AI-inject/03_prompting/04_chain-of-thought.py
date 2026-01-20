from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

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
Answer: {
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
    
"""


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Can you write the code to add n numbers in python ?",
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "START",
                    "content": "The user wants a Python function to add 'n' numbers.",
                },
            ),
        },
    ],
)

text = response.choices[0].message.content

print(text)
