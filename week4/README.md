# Week-4: Tokenizer Comparison Using BPE, WordPiece and SentencePiece

## Objective
To compare different tokenization techniques using three pretrained tokenizers and analyze how they split English, Telugu, and Hindi text into tokens.

## Requirements
- Python 3.14
- Transformers
- SentencePiece
- Hugging Face Tokenizers

## Project Structure
```text
week4/
│
├── .venv/
├── tokenizer_comparison.py
├── requirements.txt
└── README.md
```

## Implementation

1. Imported `AutoTokenizer` from the Transformers library.
2. Loaded three pretrained tokenizers:
   - BPE – GPT-2 (`gpt2`)
   - WordPiece – Multilingual BERT (`bert-base-multilingual-cased`)
   - SentencePiece – XLM-R (`xlm-roberta-base`)
3. Prepared sample text in three languages:
   - English
   - Telugu
   - Hindi
4. Loaded the pretrained tokenizers using `from_pretrained()`.
5. Tokenized each language using all three tokenizers.
6. Extracted and displayed the tokens, token IDs, and total token count.
7. Compared the tokenization results across different languages.

## Execution

Run the Python program:

```powershell
py tokenizer_comparison.py
```

## Output

The program successfully compared three tokenization methods for English, Telugu, and Hindi.

### 1. English
Input: Artificial intelligence is changing the world.

- BPE – GPT-2: 8 tokens
- WordPiece – Multilingual BERT: 10 tokens
- SentencePiece – XLM-R: 10 tokens

### 2. Telugu
Input: కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.

- BPE – GPT-2: 112 tokens
- WordPiece – Multilingual BERT: 18 tokens
- SentencePiece – XLM-R: 14 tokens

### 3. Hindi
Input: कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।

- BPE – GPT-2: 68 tokens
- WordPiece – Multilingual BERT: 17 tokens
- SentencePiece – XLM-R: 14 tokens

## Conclusion
Successfully implemented and compared BPE, WordPiece, and SentencePiece tokenization techniques using English, Telugu, and Hindi text. The experiment demonstrated that different tokenizers produce different token counts depending on the language and tokenization method.
