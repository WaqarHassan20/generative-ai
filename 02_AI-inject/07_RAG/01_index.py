from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

# Load the PDF document

loader = PyPDFLoader(file_path=str(pdf_path))

docs = loader.load()

# Split the documents into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)

chunks = text_splitter.split_documents(documents=docs)

# Create the vector embeddings using langchain and store them in a vector database

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="nodejs_docs_learning_RAG",
)

print("Indexing of documents completed ....")
