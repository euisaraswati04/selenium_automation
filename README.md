# QA Automation Portfolio – SauceDemo E-commerce

**Role focus:** Software Quality Assurance / QA Automation  
**Stack:** Python, Selenium WebDriver, Pytest  
**Application under test:** https://www.saucedemo.com/

## Project overview
This portfolio demonstrates a small end-to-end UI automation suite for a demo e-commerce application. It covers authentication, product selection, cart management, and checkout validation.

> This is an independent practice project using a publicly available demo application. It is not production testing and does not imply employment or client work.

## Skills demonstrated
- Translating user flows into test scenarios and test cases
- Automating browser interactions with Selenium WebDriver
- Using explicit waits and stable `data-test` selectors
- Organizing tests with Pytest fixtures
- Capturing screenshots when tests fail
- Reporting test results and documenting defects

## Project structure
```text
qa_selenium_portfolio/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
└── docs/
    ├── test_plan.md
    ├── test_cases.csv
    ├── test_summary_template.md
    └── bug_report_template.md
```

## Prerequisites
- Python 3.10+
- Google Chrome (or update the fixture to use another browser)
- Internet access to reach SauceDemo

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Selenium Manager (included with modern Selenium) normally handles ChromeDriver setup automatically.

## Run tests
Run all tests:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest -v tests/test_login.py
```

Run with a visible browser:
```bash
pytest -v --headed
```

The project defaults to a visible browser. For headless execution:
```bash
HEADLESS=1 pytest -v
```

## Test account
SauceDemo publishes demo credentials on its login page. This suite uses:
- Username: `standard_user`
- Password: `secret_sauce`

Do not use personal or real credentials.

## Expected coverage
| Area | Scenarios |
|---|---|
| Login | Valid login, invalid password |
| Cart | Add product, remove product |
| Checkout | Required-field validation, successful checkout |

## Important notes
- The tests depend on the demo site's availability and UI. A site update may require selector or assertion maintenance.
- The suite has been prepared as a portfolio starter. Run it locally and record the actual pass/fail results before publishing.
- Do not claim a test passed unless you have executed it and verified the result.
- Add screenshots, a real execution report, and any reproducible defects you find to make the portfolio stronger.

## Suggested GitHub description
"An independent Selenium + Python + Pytest UI automation project covering core e-commerce user journeys on SauceDemo."
