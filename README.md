# Playwright Docs Lab

A mini Python automation project using Playwright and pytest-playwright against playwright.dev as a sandbox for learning and demonstrating Playwright fundamentals.

---

## Features
- Homepage smoke test
- Navigation test using "Get started"
- Multi-tab/browser context test
- Mobile emulation test
- Page Object Model structure

---

## Tech Stack
- Python
- pytest
- pytest-playwright
- Playwright

---

## What this project demonstrates
- Navigation with `page.goto()`
- User-facing locators with `get_by_role()`
- Web-first assertions with `expect(...)`
- Page Object Model design
- Device emulation
- Multi-page browser context usage

---

## Run locally
```bash
pip install -r requirements.txt
playwright install
python -m pytest -v
