# GenAI Apps

This project demonstrates how to interact with the Google Generative AI Python SDK for various tasks, including finding place information and comparing phones.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Clone the Repository

First, clone the repository from GitHub:

`git clone https://github.com/arindewangan/genai-apps`
`cd genai-apps`



### 2. Install Required Packages

Install the required Python package using pip:

`pip install google-generativeai` 

### 3. Create a `.env` File

Create a `.env` file in the root directory of the project and add your API key in the following format:

`GEMINI_API_KEY="YOUR_API_KEY"` 

Replace `"YOUR_API_KEY"` with your actual Google Generative AI API key.

### 4. Run the Application

You can run either of the Python scripts depending on the functionality you want to use:

-   To find place information, run:
    `python run findplace.py` 
    
-   To compare phones, run:
    `python run comparephone.py`
