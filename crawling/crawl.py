import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse


def crawl_website(url, output_dir='scraped_content'):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    cleaned_text = re.sub(r'\s+', ' ', soup.get_text(separator=' ', strip=True))

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a safe filename
    parsed_url = urlparse(url=url)
    domain = parsed_url.netloc
    path = parsed_url.path.replace('/', '_').replace('\\', '_')
    filename = f"{domain}{path}.txt"

    # Full file path
    file_path = f"{output_dir}/{filename}"

    # Save cleaned text to file
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
        print(f"Content saved to: {file_path}")
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None