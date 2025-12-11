import os
from crawling import crawl
from embeddings.generate_embeddings import create_chunks, create_embeddings
from chroma.storage import save_context
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


url = "https://qualityesnad.com.sa/"
file_path = crawl.crawl_website(url)
chunks = create_chunks(file_path=file_path)
embeddings = create_embeddings(chunks=chunks)
save_context(embeddings=embeddings, chunks=chunks, content_path=file_path)
