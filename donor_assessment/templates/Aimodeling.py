import pandas as pd
import google.generativeai as genai
import os

# --- Configuration ---
# You must set your API key here. It's recommended to use an environment variable.
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not found.")
    print("Please set your API key, for example: export GEMINI_API_KEY='YOUR_API_KEY'")
    exit()

# Configure the Gemini API with your key
genai.configure(api_key=AIzaSyB09I17wkpLPDdlojwmsM2c34ha_BiwbJ0)

# The model to use. 'gemini-1.5-pro' is a powerful choice for this task.
MODEL_NAME = "gemini-1.5-pro" 

# --- Load your personal data from a CSV file ---
DATA_FILE = r"/Users/fidelmanghe/Desktop/Data.csv"
try:
    # Attempt to read the CSV file into a pandas DataFrame.
    # The 'header=None' option tells pandas to not treat the first row as headers,
    # and we manually name the columns later.
    df = pd.read_csv(DATA_FILE, header=None, names=["Category", "Description"])
    # Convert the DataFrame to a string format that can be easily included in the prompt.
    # The `to_string(index=False)` method is useful for a clean, table-like output.
    personal_data_str = df.to_string(index=False)
except FileNotFoundError:
    print(f"Error: The file '{DATA_FILE}' was not found.")
    print("Please make sure you have created the 'my_data.csv' file with your data.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the data file: {e}")
    exit()

# --- Define the prompt for the Gemini model ---
# This is a critical part of the assistant. It sets the rules for how the model should behave.
system_instruction = f"""
You are a highly specialized personal assistant. Your sole purpose is to provide information about the individual based on the following data.
You MUST NOT answer any questions that are not related to this data.
If a user asks about anything outside of this data, you must politely state that you can only answer questions about the provided information.
Your responses should be concise, helpful, and directly answer the user's query using only the information available.

Here is the data about the individual, categorized by skill, project, experience, education, and certification:
{personal_data_str}
"""

def get_gemini_response(prompt):
    """
    Sends a prompt to the Gemini model and returns the response text.
    """
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to run the personal assistant.
    """
    print("Hi! I'm your personal assistant. I can answer questions about my skills, projects, experience, and education.")
    print("Type 'exit' or 'quit' to end the conversation.")
    
    # Start the conversation loop.
    while True:
        user_query = input("\n> You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Combine the user's query with the system instruction.
        full_prompt = f"{system_instruction}\n\nUser query: {user_query}"
        
        # Get the response from the Gemini model.
        assistant_response = get_gemini_response(full_prompt)
        
        # Print the assistant's response.
        print(f"> Assistant: {assistant_response}")

if __name__ == "__main__":
    main()
