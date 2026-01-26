from fastapi import FastAPI, Body
from oolama import Client

app = FastAPI()
client = Client(host="http://localhost:11434")  # Adjust the host and port as needed,


@app.get("/")
def read_root():
    return {"message": "Welcome to the Ollama Panga server!"}


@app.get("/contact")
def contact():
    return {"Email": "myemailaddress@example.com"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/chat")
def chat(message: str = Body(..., description="Message for Ollama model")):
    response = client.chat(
        model="panga", messages=[{"role": "user", "content": message}]
    )
    return {"response": response.message.content}