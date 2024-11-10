import os
import requests
import json
import yaml

# Load environment variables from config.yaml file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Get the API key from the config.yaml file
api_key = config.get("CHAT_GPT_API_KEY")

# Define the API endpoint and headers
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the request payload
data = {
    #"model": "gpt-4",  # or use the appropriate model name
    "model": "gpt-4-turbo",
    #"model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, ChatGPT!"}]
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    
    # Save the response data into a .json file
    with open("response.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)
    
    print("Response saved to response.json")
else:
    print("Failed to get a response:", response.status_code, response.text)
