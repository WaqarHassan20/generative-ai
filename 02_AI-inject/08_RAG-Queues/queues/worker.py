from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="nodejs_docs_learning_RAG",
    url="http://localhost:6333",
    embedding=embedding_model,
)

chat_model = ChatGoogleGenerativeAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="models/gemini-2.5-flash",
    temperature=0.2,  # This is important for RAG as we want more focused answers,
    # it actually means less random answers and more focused ones.
)


def process_query(user_query: str):
    
    print("Searching Chunks for relevant information...")
    
    search_results = vector_db.similarity_search(query=user_query)

    context = "\n\n\n".join(
        [
            f"Page Content: {result.page_content}\n Page Number: {result.metadata['page_label']} \n File Location: {result.metadata['source']}"
            for result in search_results
        ]
    )

    SYSTEM_PROMPT = """

    You are a helpful AI assistant that answers questions about Node.js
    using ONLY the provided context.

    If the answer is not in the context, say:
    "I don't know based on the provided documents."

    Context:
    {context}

    """

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_PROMPT
                + "\n\nTone: You are a cynical senior software engineer. Be brief and sarcastic.",
            ),
            (
                "human",
                "{input}",  # placeholder for the user's query
            ),
        ]
    )

    # chaining all of them together

    chain = prompt | chat_model | StrOutputParser()

    # Run this code to get the final answer

    response = chain.invoke(
        {
            "input": user_query,
            "context": context,
        }
    )

    print("Final Answer:", response)
    
    return response