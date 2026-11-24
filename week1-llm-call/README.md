# Week-1: LLM Call Using Gemini API

## Objective
To connect a Python program with Google's Gemini API, send a prompt to a Large Language Model (LLM), and display the generated response.

## Requirements
- Python
- Gemini API Key
- Internet Connection
- Google GenAI Library
- Python-dotenv Library

## Project Structure
```text
week1-llm-call/
│
├── .venv/
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Implementation
1. Load the API key from the `.env` file using `load_dotenv()`.
2. Initialize the Gemini client using the API key.
3. Prepare a prompt: "What is Artificial Intelligence? Explain in simple words."
4. Connect to the Gemini model `gemini-3.8-flash`.
5. Retry the request if the model returns a 503 UNAVAILABLE error.
6. Use `gemini-3.5-flash-lite` as a backup model.
7. Display the generated response in the terminal.

## Execution
Run the following command:

```powershell
py main.py
```

## Output
- The first model (`gemini-3.8-flash`) returned a 503 UNAVAILABLE error due to high demand.
- The program retried after 5 seconds.
- The backup model (`gemini-3.5-flash-lite`) successfully generated the response.
- The response explained Artificial Intelligence in simple words.
- Examples included Netflix/YouTube recommendations, Siri/Alexa, and video games.

## Conclusion
Successfully implemented a Python-based LLM API call using Google's Gemini API. The program demonstrated prompt processing, response generation, retry handling, and backup model selection.
