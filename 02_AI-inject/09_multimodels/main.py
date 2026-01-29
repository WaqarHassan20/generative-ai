from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in the image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.pexels.com/photos/28346096/pexels-photo-28346096.jpeg"
                    },
                },
            ],
        }
    ],
)

text = response.choices[0].message.content

print(text)


# ➜ ~/Desktop/programming/generative-ai/02_AI-inject (main) uv run 09_multimodels/main.py
# This image captures a woman standing on a sandy beach at what appears to be either sunrise or sunset, given the warm, golden light.

# Here's a detailed breakdown:

# *   **Subject:** A woman with dark skin and long, straight, dark hair, parted down the middle. She is wearing a red two-piece bikini.
# *   **Pose and Expression:** She is standing, facing slightly to her right (viewer's left), with her left hand raised to her forehead, shielding her eyes as if looking into the sun or searching in the distance. Her gaze is directed off-frame to the right. Her expression is serene and contemplative.
# *   **Details:**
#     *   She has several visible tattoos: "1994" is tattooed on her mid-torso, just below her left breast. There's a circular tattoo on her upper right arm/bicep, and other smaller, less distinct tattoos on her forearms (one on her right forearm appears to be a stylized rabbit or similar animal).
#     *   She wears a delicate bracelet on her right wrist and a ring on her left index finger. Her fingernails have a light, possibly white or pale pink, polish.
#     *   Noticeable tan lines are visible around her bikini bottom, indicating a different or slightly smaller swimsuit might have been worn previously.
# *   **Setting:**
#     *   **Foreground:** Wet, reflective sand with ripples and small water puddles where the ocean meets the shore.
#     *   **Midground:** The ocean with gentle waves lapping the beach. The water is a deep blue-grey.
#     *   **Background:** Distant hills or mountains covered in brownish-green foliage, blurring into the hazy horizon under a pale, light blue sky.
# *   **Lighting and Atmosphere:** The scene is bathed in warm, directional light, casting strong shadows and highlighting the woman's figure and the texture of the sand. The overall impression is calm, natural, and bathed in a golden hour glow. The image has a subtle film grain, giving it a somewhat vintage or artistic feel.
