import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Upload the image file
files = [
  upload_to_gemini("D:\\Smartphone Comparison\\india-gate.jpeg", mime_type="image/jpeg"),
]

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
        "What is this place and Where is it? Give me Place Name, CIty, State and Country",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"Place Name\": \"Vidhana Soudha\", \"City\": \"Bengaluru\", \"State\": \"Karnataka\", \"Country\": \"India\"}\n\n```",
      ],
    },
  ]
)

response = chat_session.send_message("What is this place and Where is it? Give me Place Name, CIty, State and Country")

data = json.loads(response.text)

for key, value in data.items():
    print(f"{key}: {value}")