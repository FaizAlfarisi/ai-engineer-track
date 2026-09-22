# Expense / Transaction Manager CLI

A simple CLI application for managing income and expenses with JSON persistence and CSV reports.

## Requirements

* Python 3
* mypy

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install mypy
python -m pip freeze > requirements.txt

```

## Usage

### Add transaction

```bash
python main.py add DATE CATEGORY KIND AMOUNT

```

Example:

```bash
python main.py add 2026-09-12 lunch expense 25000

```

### List transactions

```bash
python main.py list

```

### Monthly report

```bash
python main.py report monthly

```

Creates `monthly.csv` with the net amount for each month.

### Category report

```bash
python main.py report categories

```

Creates `categories.csv` with the net amount for each category.

## Data

* Transactions are stored in `transactions.json`.
* Generated Reports:
* `monthly.csv`
* `categories.csv`



## Type Check

```bash
.venv\Scripts\python -m mypy main.py

```

## Project Structure

```text
.
├── main.py
├── transactions.json
├── monthly.csv
├── categories.csv
├── requirements.txt
├── .gitignore
└── README.md

```