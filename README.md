# Selenium Website Test Automation

This project automates validation of the portfolio website navigation and a 404 page check using Selenium.

## Features

- Verifies all main navigation links on the homepage
- Checks the undefined URL behavior for a 404 response
- Saves a screenshot for the 404 page
- Logs execution details in the `logs` folder

## Requirements

- Python 3.9+
- Google Chrome installed and available in PATH
- Selenium and Requests

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Output

- Logs are written to the `logs/` directory
- Screenshots are saved in the `screenshots/` directory
