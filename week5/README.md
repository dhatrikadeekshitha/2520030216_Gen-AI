# Week-5: Token Economics and Budget Estimation

## Objective
To develop a Python-based Token Economics Calculator that estimates daily and monthly LLM usage costs, calculates token consumption, checks RPM and TPM capacity, and validates budget limits.

## Requirements
- Python 3.14
- Python-dotenv

## Project Structure
```text
TokenEconomics/
│
├── .venv/
├── .env
├── budget.py
├── test_budget.py
├── requirements.txt
└── README.md
```

## Implementation

1. Created a `FeatureBudget` dataclass to manage LLM usage and budget parameters.
2. Loaded configuration values from the `.env` file using `python-dotenv`.
3. Calculated daily input tokens and output tokens.
4. Calculated total daily token consumption.
5. Estimated daily and monthly API costs based on input and output token pricing.
6. Calculated peak Requests Per Minute (RPM) and Tokens Per Minute (TPM) with a safety margin.
7. Checked RPM capacity, TPM capacity, daily budget, and monthly budget.
8. Displayed a recommendation based on the budget and capacity checks.
9. Implemented unit tests using Python's unittest framework.

## Execution

Run the program:

```powershell
python budget.py
```

Run unit tests:

```powershell
py -m pytest -v
```

## Output

The program generated the following Token Economics Report:

### Usage Estimation
- Input Tokens/Day: 2,400,000
- Output Tokens/Day: 600,000
- Total Tokens/Day: 3,000,000

### Cost Estimation
- Estimated Daily Cost: $1.4400
- Estimated Monthly Cost: $43.20

### Capacity Estimation
- Peak RPM with Margin: 36
- Peak TPM with Margin: 54,000

### Validation Checks

| Check | Result |
|---|---|
| RPM Capacity | PASS |
| TPM Capacity | PASS |
| Daily Budget | PASS |
| Monthly Budget | REVIEW |

**Recommendation:** Revise assumptions, limits, or design before build.

## Unit Testing
The test file verifies:
- Daily and monthly cost calculations.
- RPM and TPM capacity validation.
- RPM limit failure handling.
- Monthly budget failure handling.

## Conclusion
Successfully developed a Token Economics Calculator to estimate LLM token consumption, API costs, and capacity requirements. The application validates daily and monthly budgets and provides recommendations before deploying an LLM-based application.
