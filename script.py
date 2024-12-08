import os
import sys
import requests
import json
import yaml

# Function to load environment variables from config.yaml file
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

# Function to send a request to the ChatGPT API
def send_request(api_key, file_content, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the request payload
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You are processing a document and a user-provided prompt."},
            {"role": "user", "content": f"Document content:\n{file_content}\n\nPrompt:\n{prompt}"}
        ]
    }

    # Send the request
    response = requests.post(url, headers=headers, json=data)

    return response

# Function to read a file's content
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

# Main script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_pdf_file> <path_to_prompt_file>")
        sys.exit(1)

    # Get file paths from command-line arguments
    document_path = sys.argv[1]
    prompt_path = sys.argv[2]

    # Load the configuration
    config = load_config()
    api_key = config.get("CHAT_GPT_API_KEY")

    if not api_key:
        print("Error: API key not found in config.yaml")
        sys.exit(1)

    # Read the files
    document_content = read_file(document_path)
    prompt_content = read_file(prompt_path)

    # Send the request
    response = send_request(api_key, document_content, prompt_content)

    # Process the response
    if response.status_code == 200:
        response_data = response.json()

        # Save the response data into a .json file
        with open("response.json", "w") as json_file:
            json.dump(response_data, json_file, indent=4)

        print("Response saved to response.json")
    else:
        print(f"Failed to get a response: {response.status_code}\n{response.text}")
