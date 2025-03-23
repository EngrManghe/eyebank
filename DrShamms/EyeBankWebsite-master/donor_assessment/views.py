import os
import uuid
import json
import requests
import yaml
import glob

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .models import UploadedFile
from PyPDF2 import PdfReader

UPLOADS_DIR = "EyeBankWebsite/media/uploads/"

def home(request):
    return render(request, "home.html")

def upload_file(request):
    if request.method == "POST" and request.FILES.get("donor_file"):
        uploaded_file = request.FILES["donor_file"]
        
        # Ensure media directory exists
        upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(upload_dir, exist_ok=True)

        # Generate a unique filename
        file_extension = uploaded_file.name.split(".")[-1]
        file_name = f"donor_record_{uuid.uuid4().hex}.{file_extension}"
        file_path = os.path.join(upload_dir, file_name)

        # Save the file
        with open(file_path, "wb") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        return JsonResponse({"message": "File uploaded successfully!", "filename": file_name})

    return JsonResponse({"error": "Failed to upload file"}, status=400)

def get_prompt(request):
    prompt_id = request.GET.get("prompt_id")
    prompt_file = os.path.join(settings.BASE_DIR, f"donor_assessment/prompts/prompt{prompt_id}.txt")
    
    if os.path.exists(prompt_file):
        with open(prompt_file, "r", encoding="utf-8") as f:
            content = f.read()
        return JsonResponse({"prompt": content})
    
    return JsonResponse({"error": "Prompt not found"}, status=404)

@csrf_exempt
def submit_question(request):
    if request.method == 'POST':
        # Handle file upload
        if "donor_file" in request.FILES:
            uploaded_file = request.FILES["donor_file"]
            # Ensure media directory exists
            upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
            os.makedirs(upload_dir, exist_ok=True)

            # Generate a unique filename
            file_extension = uploaded_file.name.split(".")[-1]
            uniqueuuid = uuid.uuid4()
            file_name = f"donor_record_{uniqueuuid.hex}.{file_extension}"
            file_path = os.path.join(upload_dir, file_name)

            # Save the file
            with open(file_path, "wb") as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # Extract text from the PDF
            pdf_content = extract_text_from_pdf(file_path)

            # Handle question submission
            prompt_id = request.POST.get("prompt_id", "")
            if prompt_id:
                # Load the prompt content
                prompt_file = os.path.join(settings.BASE_DIR, f"donor_assessment/prompts/prompt{prompt_id}.txt")
                if os.path.exists(prompt_file):
                    with open(prompt_file, "r", encoding="utf-8") as f:
                        prompt_content = f.read()

                    # Send request to ChatGPT API
                    config_path = os.path.join(settings.BASE_DIR, 'config.yaml')

                    # Load the configuration
                    with open(config_path, 'r') as file:
                        config = yaml.safe_load(file)

                    # Access the API key
                    api_key = config.get('CHAT_GPT_API_KEY')
                    print(api_key)
                    response = send_request(api_key, pdf_content, prompt_content)

                    if response.status_code == 200:
                        response_data = response.json()
                        # Extract the content field from the response
                        content = response_data.get("choices", [])[0].get("message", {}).get("content", "")
                        if content:
                            try:
                                structured_data = json.loads(content.strip("```json\n").strip("```"))
                                # Save the structured data as a JSON file
                                json_file_name = f"structured_data_{uniqueuuid.hex}.json"
                                json_file_path = os.path.join(upload_dir, json_file_name)
                                with open(json_file_path, "w") as json_file:
                                    json.dump(structured_data, json_file, indent=4)
                                return JsonResponse({"message": "File processed successfully!", "data": structured_data})
                            except json.JSONDecodeError as e:
                                return JsonResponse({"error": f"Error decoding JSON content: {e}"}, status=500)
                        else:
                            return JsonResponse({"error": "No content found in API response"}, status=500)
                    else:
                        return JsonResponse({"error": f"Failed to get a response: {response.status_code}\n{response.text}"}, status=500)
                else:
                    return JsonResponse({"error": "Prompt file not found"}, status=404)
            else:
                return JsonResponse({"error": "No question selected"}, status=400)
        else:
            return JsonResponse({"error": "No file uploaded"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def extract_text_from_pdf(pdf_path):
    """This function extract pdf content and transform it into text"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF file {pdf_path}: {e}")
        return ""

def send_request(api_key, document_content, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are analyzing a document and responding to a prompt."},
            {"role": "user", "content": f"Document content:\n{document_content}\n\nPrompt:\n{prompt}"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response

def get_latest_json(request):
    json_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    json_files = sorted(glob.glob(os.path.join(json_dir, 'structured_data_*.json')), key=os.path.getmtime, reverse=True)

    if not json_files:
        return JsonResponse({"error": "No JSON files found"}, status=404)

    with open(json_files[0], 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Ensure the data is serializable and set `safe=False` if it's a list
    return JsonResponse(data, safe=isinstance(data, dict))
