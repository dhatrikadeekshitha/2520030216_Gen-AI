
import os
import time
from dotenv import load_dotenv
from google import genai

# Step 1: Load API key from .env
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Gemini API key not found! Check your .env file."
    )

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Prepare the prompt
prompt = "What is Artificial Intelligence? Explain in simple words."

# Step 5: Try the lab model, then the backup model
models = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite"
]

response = None

for model in models:
    for attempt in range(2):
        try:
            print(f"Connecting to {model}...")

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                print("\nLLM Response:")
                print(response.text)
            else:
                print("The model returned an empty response.")

            break

        except Exception as e:
            error_message = str(e)

            print(f"Attempt {attempt + 1} failed: {error_message}")

            if "503" in error_message or "UNAVAILABLE" in error_message:
                if attempt == 0:
                    print("Retrying in 5 seconds...")
                    time.sleep(5)
                    continue

            break

    if response is not None:
        break

if response is None:
    print("\nUnable to get a response from Gemini.")
    print("Please check your internet, API key, quota, and model availability.")
