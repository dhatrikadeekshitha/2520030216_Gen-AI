# Week-2: LLM Client with Multiple Providers (Gemini & Ollama)

## Objective
To develop a common LLM client that supports multiple providers, including Google Gemini (Cloud-based) and Ollama (Local LLM), using Python.

## Requirements
- Python 3.14
- Gemini API Key
- Ollama
- Google GenAI Library
- Python-dotenv
- Requests
- Pytest

## Project Structure
```text
week2/
│
├── .venv/
├── .env
├── .gitignore
├── main.py
├── llm_client.py
├── test_client.py
└── requirements.txt
```

## Implementation

1. Created a common `LLMProvider` abstract class to define the generate() method.
2. Implemented `GeminiProvider` to connect with Google's Gemini API.
3. Implemented `OllamaProvider` to generate responses using the local Llama 3.2 model.
4. Created an `LLMClient` class to handle different providers through a common interface.
5. Added automatic retry handling and fallback models for temporary Gemini server errors.
6. Used environment variables to securely manage the Gemini API key.
7. Implemented unit testing using Pytest to verify LLM client functionality.

## Execution

Run the test file:

```powershell
py -m pytest -v
```

Run the main program:

```powershell
py main.py
```

Choose the provider:

```text
Choose provider (gemini/ollama):
```

Enter your question to generate the response.

## Output

### 1. Gemini Provider
- The primary model `gemini-3.8-flash` was temporarily unavailable.
- The program automatically retried the request.
- Successfully connected to the backup model `gemini-3.5-flash-lite`.
- Generated a response explaining Machine Learning with examples such as teaching a computer to recognize a dog and Netflix recommendations.

### 2. Ollama Provider
- Successfully connected to the local Ollama model `llama3.2`.
- Generated a response explaining Artificial Intelligence.
- Explained AI concepts, working, types, and benefits.

### 3. Unit Testing
- Executed tests using Pytest.
- `test_generate` passed successfully.
- Result: **1 passed**.

## Conclusion
Successfully implemented a multi-provider LLM client using Gemini and Ollama. The project demonstrates abstraction, provider switching, automatic retry handling, local and cloud-based LLM integration, and unit testing.
