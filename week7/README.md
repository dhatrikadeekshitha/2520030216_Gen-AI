# Week-7: Next-Token Probability Analysis Using GPT-2

## Objective

To inspect how a language model predicts the next token for a given prompt by examining model logits, converting them into probabilities, and identifying the top-k most likely next-token candidates.

## Requirements

- Python 3.14
- PyTorch
- Transformers Library
- CSV
- Internet connection for the first-time download of the GPT-2 model

## Project Structure
```text
week7/
│
├── .venv/
├── main.py
├── week7_probability_results.csv
├── requirements.txt
└── README.md
```

## Implementation

1. Imported the required libraries: PyTorch, CSV, and Transformers.
2. Selected the pre-trained GPT-2 model (`openai-community/gpt2`).
3. Loaded the model and its tokenizer using the Transformers library.
4. Defined four input prompts:
   - The cat is
   - Artificial intelligence is
   - India is a
   - Machine learning helps
5. Tokenized each prompt and displayed its input token IDs.
6. Passed the tokenized input to GPT-2 and obtained the model's output logits.
7. Selected the logits for the next-token position.
8. Applied the softmax function to convert logits into probability values.
9. Used Top-K selection with `TOP_K = 5` to identify the five most probable next-token candidates for each prompt.
10. Displayed each candidate token, its rank, token ID, and probability.
11. Saved the results in `week7_probability_results.csv`.

## Execution

Install the required libraries:
```bash
py -m pip install -r requirements.txt
```

Run the program:
```bash
py main.py
```

The first execution may take some time because the GPT-2 model and tokenizer need to be downloaded.

## Output

### Next-Token Probability Analysis

- Model: GPT-2 (`openai-community/gpt2`)
- Total Prompts: 4
- Top-K Candidates per Prompt: 5
- Total Candidate Records: 20
- Output File: `week7_probability_results.csv`

### Evaluation Results

For each prompt, the program displays:

- Input token IDs
- Top 5 next-token candidates
- Rank of each candidate
- Candidate token
- Token ID
- Probability of each candidate

The CSV file stores 5 candidate records for each of the 4 prompts, giving a total of 20 records.

## Output File

The results are saved in:
```text
week7_probability_results.csv
```

The CSV file contains:

- Prompt
- Rank
- Candidate Token
- Token ID
- Probability

## Conclusion

Successfully implemented a next-token probability analysis system using the GPT-2 language model. The program processed four prompts, examined the model's logits, converted them into probability values using softmax, and identified the top five next-token candidates for each prompt. The results were displayed and saved in CSV format for further analysis.
