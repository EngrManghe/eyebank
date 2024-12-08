import json

# Load the response.json file
with open("response.json", "r") as file:
    response_data = json.load(file)

# Navigate to the 'content' field
content = response_data.get("choices", [])[0].get("message", {}).get("content", "")

if content:
    # Clean and format the extracted content
    try:
        structured_data = json.loads(content.strip("```json\n").strip("```"))
        
        # Save the structured content to a new file
        with open("structured_content.json", "w") as output_file:
            json.dump(structured_data, output_file, indent=4)
        print("Structured content saved to structured_content.json")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON content: {e}")
else:
    print("Content not found in response.json")
