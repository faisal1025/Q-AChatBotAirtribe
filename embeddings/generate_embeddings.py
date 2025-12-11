from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_chunks(file_path, chunk_size=1000, chunk_overlap=200):    
    try:
        with open(file=file_path, mode='r', encoding='utf-8') as file:
            content = file.read()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            separators=["\n\n", "\n", " ", ""],
            chunk_overlap=chunk_overlap,
            length_function=len
        )

        chunks = text_splitter.split_text(content)
        return chunks
    except FileNotFoundError:
        print(f"Error: file {file_path} not found")
        return []
    except Exception as e:
        print(f"Error: reading file {e}")
        return []

def create_embeddings(chunks):
    if not chunks:
        print("No chunks created, skipping embeddings")
        return []
    try:

        embedding_response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunks,
            encoding_format="float"
        )

        vectors = [item.embedding for item in embedding_response.data]
        print(f"Got, {len(vectors)} embeddings, each of length {len(vectors[0])}")

        return vectors
    except Exception as e:
        print(f"Error: unable to create embeddings {e}")
        return []
