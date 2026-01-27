from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def main():
    user_query = input("Enter your query : ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": user_query}],
    )
    print("Response : ", response.choices[0].message.content)


if __name__ == "__main__":
    main()

# FIRST RESPONSES OF THE CODE:

# (02_AI-inject) ➜ ~/Desktop/programming/generative-ai/02_AI-inject (main) uv run 06_weather-agenticAI/main.py                  
# Enter your query : what is temperature of lahore ?
# Response :  I need a bit more information to give you the current temperature of Lahore. Is it possible for you to specify:
# *   **When** you want the temperature for? (e.g., right now, this morning, this afternoon, tonight)
# Once you provide that, I can give you a more accurate answer!

# ==========================================================================================================================

# SECOND RESPONSES OF THE CODE:

# (02_AI-inject) ➜ ~/Desktop/programming/generative-ai/02_AI-inject (main) uv run 06_weather-agenticAI/main.py
# Enter your query : what is temperature of lahore right now ?
# Response :  I cannot provide real-time temperature information for Lahore. My knowledge base is not updated with live data.
# To get the current temperature in Lahore, I recommend checking a reliable weather source like:
# *   **A weather app on your smartphone:** Most phones come with a built-in weather app.
# *   **A weather website:** Popular options include AccuWeather, The Weather Channel, or Google Weather (you can just search "weather Lahore").
# *   **A local news website or TV channel:** They often have live weather updates.

# https://wttr.in/{city}?format=%C+%t