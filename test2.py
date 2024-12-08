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
    "model": "gpt-3.5-turbo",
    #"model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello, ChatGPT!"}]
}

# Define the SOCKS5 proxy with authentication
proxy_host = "85.195.81.165"
proxy_port = "11682"
proxy_username = "y2kDfM"
proxy_password = "SdW0Cz"

proxies = {
    "http": f"socks5://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}",
    "https": f"socks5://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
}

# Send the request using the proxy
try:
    #response = requests.post(url, headers=headers, json=data, proxies=proxies, timeout=30)
    response = requests.post(url, headers=headers, json=data, timeout=30)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
    response_data = response.json()

    with open("response.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)

    print("Response saved to response.json")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
