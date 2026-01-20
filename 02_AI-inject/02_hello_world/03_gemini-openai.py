from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    # model="gemma-3-12b",
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "system",
            "system": "You are an expert in Maths and only answers related to Maths. And if the question is not related to math, reply with 'I can only answer math questions'",
        },
        # Since my Gemini API key is not paid, so it is not bounded my me so not giving me expected answers.
        {
            "role": "user",
            # "content": "What is the integral of x^2?",
            "content": "What is the code to print hello in python ?",
        },
    ],
)

text = response.choices[0].message.content

print(text)