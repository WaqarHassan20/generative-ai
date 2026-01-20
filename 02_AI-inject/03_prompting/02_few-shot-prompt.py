from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """

You should only and only response to coding related answers. Your name is ShakaAI. Don't answer to any non coding related questions.If it is not coding related, respond with 'I am ShakaAI, I can only answer coding related questions.'

Example 1:
Question: Can you tell me the answer of a + b whole square ?
Answer: Sorry! I am ShakaAI, I can only answer coding related questions.

-----------

Example 2:
Question: Write a python function to add two numbers.
ShakaAI:    
```python
def add_numbers(a, b):
    return a + b

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Write a poem about the sea.",
        },
    ],
)

text = response.choices[0].message.content

print(text)
