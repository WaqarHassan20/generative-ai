from dotenv import load_dotenv
from google import genai
from mem0 import Memory
import json
import os

load_dotenv()

NEO_CONNECTION_URI = os.getenv("NEO_CONNECTION_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEO_PASSWORD = os.getenv("NEO_PASSWORD")

client = genai.Client(api_key=GEMINI_API_KEY)

# As there was no free model for embeddings in Gemini, so this code is not saving
# the embeddings in the vector store. But the structure is here for reference.
# And rest of code is working fine.

config = {
    "memory": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {"api_key": GEMINI_API_KEY, "model": "gemini-embedding-1.0"},
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.5-flash-lite",
            "temperature": 0.2,
        },
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO_CONNECTION_URI,
            "username": "neo4j",
            "password": NEO_PASSWORD,
        },
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": "6333"},
    },
}

memory_client = Memory.from_config(config)


while True:

    user_query = input("Ask a question : ")

    search_memory = memory_client.search(query=user_query, user_id="shakalaka")

    memories = [
        f"ID: {mem.get("id")} \n Content: {mem.get("content")}"
        for mem in search_memory.get("results")
    ]

    print("Memories found: ", memories)

    SYSTEM_PROMPT = f"""
    You are a helpful AI assistant who answers user query based on the available context retrieved from the conversation memory.
    You should only answer the user based on the following context.
    Context:
    {json.dumps(memories)}
    """

    ai_response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_query
    )

    print("AI Response: ", ai_response.text)

    print("Saving to memory...")

    memory_client.add(
        user_id="shakalaka",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_query,
            },
        ],
    )

    print("Saved to memory")
