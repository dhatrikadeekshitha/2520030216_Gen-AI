# Week-6: LLM Baseline Evaluation Using Golden Question Set

## Objective
To evaluate the performance of an LLM using a predefined Golden Question Set and measure response quality through keyword-based scoring.

## Requirements
- Python 3.14
- Ollama
- Llama 3.2 Model
- Requests Library
- JSON
- CSV

## Project Structure
```text
week6/
│
├── .venv/
├── golden_set.json
├── main.py
├── baseline_results.csv
├── requirements.txt
└── README.md
```

## Implementation

1. Created a Golden Question Set containing 30 questions, expected answers, keywords, and reference sources.
2. Integrated the local Ollama model `llama3.2`.
3. Generated LLM responses for each question using the Ollama API.
4. Implemented keyword-based scoring to compare generated responses with expected keywords.
5. Calculated matched keywords, missing keywords, and keyword coverage percentage.
6. Assigned PASS status for scores of 60% or above and REVIEW status for scores below 60%.
7. Stored evaluation results in a CSV file named `baseline_results.csv`.
8. Generated a baseline evaluation summary with average keyword coverage and response statistics.

## Execution

Run the program:

```powershell
py main.py
```

## Output

### Baseline Evaluation Summary

- Release Version: v0.1
- Model: llama3.2
- Total Questions: 30
- Successful Responses: 30
- Passed Questions: 13
- Questions for Review: 17
- Failed Requests: 0
- Average Keyword Coverage: 50.28%

### Evaluation Results

| Metric | Result |
|---|---:|
| Total Questions | 30 |
| Successful Responses | 30 |
| Passed Questions | 13 |
| Review Questions | 17 |
| Failed Requests | 0 |
| Average Keyword Coverage | 50.28% |

## Output File
The evaluation results are saved in:

```text
baseline_results.csv
```

The CSV file contains:
- Question ID
- Question
- Expected Answer
- LLM Answer
- Matched Keywords
- Missing Keywords
- Score
- Status
- Source
- Model
- Release Version

## Conclusion
Successfully implemented a baseline evaluation system using Ollama and a Golden Question Set. The system evaluated 30 questions, calculated keyword coverage, classified responses as PASS or REVIEW, and saved the results in CSV format for further analysis.
