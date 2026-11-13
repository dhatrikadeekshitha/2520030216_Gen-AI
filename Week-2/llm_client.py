
from abc import ABC, abstractmethod
import time
from google import genai
import requests


# Common interface
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# Gemini cloud provider
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

        # Primary model followed by fallback models
        self.models = [
            "gemini-3.8-flash",
            "gemini-3.5-flash-lite",
            "gemini-3.7-flash"
        ]

    def generate(self, prompt):

        last_error = None

        for model in self.models:

            print(f"\nTrying Gemini model: {model}")

            for attempt in range(2):

                try:
                    response = self.client.models.generate_content(
                        model=model,
                        contents=prompt
                    )

                    if not response.text:
                        raise RuntimeError(
                            "Gemini returned an empty response."
                        )

                    print(f"Successfully connected to {model}")
                    return response.text

                except Exception as error:

                    last_error = error
                    error_message = str(error).lower()

                    temporary_errors = [
                        "503",
                        "unavailable",
                        "500",
                        "502",
                        "504",
                        "high demand"
                    ]

                    if any(
                        message in error_message
                        for message in temporary_errors
                    ):

                        if attempt == 0:
                            print("Temporary server issue. Retrying...")
                            time.sleep(3)
                        else:
                            print(
                                f"{model} is temporarily unavailable."
                            )
                            break

                    else:
                        raise RuntimeError(
                            "Gemini request failed. Check your API key, "
                            "model access and API quota."
                        ) from None

        raise RuntimeError(
            "Gemini servers are currently unavailable. "
            "Please try again later or select Ollama."
        ) from last_error


# Ollama local provider
class OllamaProvider(LLMProvider):

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            return response.json()["response"]

        except requests.RequestException:
            raise RuntimeError(
                "Cannot connect to Ollama. "
                "Make sure Ollama is running."
            ) from None


# Common client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
