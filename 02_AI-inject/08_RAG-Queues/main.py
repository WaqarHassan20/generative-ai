from dotenv import load_dotenv
from server import app
import uvicorn
import os

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)