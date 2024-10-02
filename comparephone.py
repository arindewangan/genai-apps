import os
import google.generativeai as genai
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
)

# Ask for user input
phone1 = input("Enter the name of the first phone: ")
phone2 = input("Enter the name of the second phone: ")

# Start the chat session
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                f"Compare the Phone 1 - Iphone 6s with Phone 2 - Iphone 14. Give Performance, Display, Front Camera, Back Camera, Battery, Storage, and Price",
            ],
        },
        {
            "role": "model",
            "parts": ["json\n{\"Phone 1\": {\"Performance\": \"Apple A9 chip with 2GB RAM\", \"Display\": \"4.7 inches, 750 x 1334 pixels, IPS LCD\", \"Front Camera\": \"5 MP, f/2.2\", \"Back Camera\": \"12 MP, f/2.2\", \"Battery\": \"1715 mAh\", \"Storage\": \"16GB, 64GB, 128GB\", \"Price\": \"Discontinued, but used models are available for around $100-$200\"}, \"Phone 2\": {\"Performance\": \"Apple A16 Bionic chip with 6GB RAM\", \"Display\": \"6.1 inches, 2532 x 1170 pixels, OLED with 60Hz refresh rate\", \"Front Camera\": \"12 MP, f/2.2\", \"Back Camera\": \"48 MP main, 12 MP ultrawide, 12 MP telephoto\", \"Battery\": \"3850 mAh\", \"Storage\": \"128GB, 256GB, 512GB\", \"Price\": \"Starts at around $799\"}}\n\n",
      ],
    },
    ]
)

# Get the comparison
response = chat_session.send_message(f"Compare the Phone 1 - {phone1} with Phone 2 - {phone2}. Give Performance, Display, Front Camera, Back Camera, Battery, Storage, and Price")
comparison = response.text

# Convert the response to a dictionary
comparison_data = json.loads(comparison)

def print_comparison(phone_label, phone_name, phone_data):
    print(f"\n{'*'*40}")
    print(f"{phone_label} ({phone_name}):")
    for spec, value in phone_data.items():
        print(f"{spec}: {value}")
    print(f"{'*'*40}\n")

print(f"\nComparison of {phone1} and {phone2}:\n")

# Check if Phone 1 and Phone 2 exist in the parsed data
if "Phone 1" in comparison_data:
    print_comparison("Phone 1", phone1, comparison_data["Phone 1"])

if "Phone 2" in comparison_data:
    print_comparison("Phone 2", phone2, comparison_data["Phone 2"])