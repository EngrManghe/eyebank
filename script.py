import os
import sys
import requests
import json
import yaml
from PyPDF2 import PdfReader

# Function to load environment variables from config.yaml file
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF file {pdf_path}: {e}")
        sys.exit(1)

# Function to read a text file
def read_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading text file {file_path}: {e}")
        sys.exit(1)

# Function to send a request to the ChatGPT API
def send_request(api_key, document_content, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        #"model": "gpt-4-turbo",
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are analyzing a document and responding to a prompt."},
            {"role": "user", "content": f"Document content:\n{document_content}\n\nPrompt:\n{prompt}"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response

# Main script logic
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_pdf_file> <path_to_prompt_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    prompt_path = sys.argv[2]

    # Load API key from config
    config = load_config()
    api_key = config.get("CHAT_GPT_API_KEY")
    if not api_key:
        print("Error: API key not found in config.yaml")
        sys.exit(1)

    # Extract content from the PDF
    pdf_content = extract_text_from_pdf(pdf_path)

    # Read prompt from file
    prompt_content = read_text_file(prompt_path)

    # Send the request
    response = send_request(api_key, pdf_content, prompt_content)

    # Process the response
    if response.status_code == 200:
        response_data = response.json()
        with open("response.json", "w") as json_file:
            json.dump(response_data, json_file, indent=4)
        print("Response saved to response.json")
    else:
        print(f"Failed to get a response: {response.status_code}\n{response.text}")
