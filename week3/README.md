# Week-3: LLM Usage Monitoring and Token Economics

## Objective
To develop a multi-provider LLM application using Gemini and Ollama with usage monitoring, token counting, latency measurement, cost estimation, and MongoDB integration.

## Requirements
- Python 3.14
- Gemini API Key
- Ollama (Llama 3.2)
- MongoDB
- Google GenAI
- PyMongo
- Requests
- Python-dotenv
- Pytest

## Project Structure
```text
week3/
│
├── .venv/
├── .env
├── .gitignore
├── main.py
├── llm_client.py
├── usage_logger.py
├── test_client.py
└── requirements.txt
```

## Implementation

1. Created an abstract LLM provider interface to support Gemini and Ollama.
2. Implemented Gemini with automatic fallback between multiple models.
3. Integrated Ollama using the local Llama 3.2 model.
4. Developed a common LLM client to handle API requests.
5. Implemented token usage tracking for input and output tokens.
6. Measured response latency in milliseconds.
7. Estimated API cost based on token usage and configured pricing.
8. Integrated MongoDB to store LLM usage details.
9. Implemented retry handling for temporary server and connection errors.
10. Added unit testing to verify response generation and usage logging.

## Execution

Run the application:

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
- The primary model `gemini-3.8-flash` returned a 503 UNAVAILABLE error.
- The application switched to the backup model `gemini-3.7-flash`.
- The second model was also temporarily unavailable.
- Successfully connected to `gemini-3.5-flash-lite`.
- Generated a response explaining Machine Learning using a dog-recognition example.
- Usage details were successfully saved to MongoDB.

**Observed Metrics:**
- Latency: 46936.89 ms
- Input Tokens: 8
- Output Tokens: 412
- Estimated Cost: $0.0

### 2. Ollama Provider
- Successfully connected to the local `llama3.2` model.
- Generated a response explaining Machine Learning with a coffee shop example.
- Usage details were successfully saved to MongoDB.

**Observed Metrics:**
- Latency: 32913.08 ms
- Input Tokens: 38
- Output Tokens: 338
- Estimated Cost: $0.0

### 3. Unit Testing
- Executed unit tests using Pytest.
- Verified response generation and usage logging.
- Checked token counting and successful request status.

## Conclusion
Successfully implemented an LLM usage monitoring system using Gemini, Ollama, and MongoDB. The application measures token consumption, response latency, and estimated cost while supporting model fallback, error handling, and usage tracking.
