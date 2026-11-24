# Week-7: Autoregressive Text Generation Using Python

## Objective
To implement a simple autoregressive text generation model that predicts the next word based on previously available words and generates a sequence of text.

## Requirements
- Python 3.14
- Random module (built-in Python library)

## Project Structure
```text
week7/
│
├── autoregression.py
└── README.md
```

## Implementation

1. Created a sample training dataset containing sentences related to students and teachers.
2. Converted the text into lowercase words using tokenization.
3. Built a next-word probability dictionary by storing the words that follow each current word.
4. Implemented a `generate_text()` function for autoregressive text generation.
5. Used `random.choice()` to select the next word from the available words.
6. Generated text starting with the word `"the"` for a maximum of 10 additional words.
7. Displayed the generated text in the terminal.

## Execution

Run the Python program:

```powershell
py autoregression.py
```

## Output

```text
Generated Text:
the teacher taught students the student passed examination the student passed
```

The generated sentence may change each time because the program randomly selects the next word based on the training text.

## Conclusion
Successfully implemented a simple autoregressive text generation model using Python. The program demonstrates tokenization, next-word selection, and sequential text generation using previously learned word patterns.
