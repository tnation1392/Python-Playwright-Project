# Playwright Docs Lab

A mini Python automation project using Playwright and pytest-playwright against playwright.dev as a sandbox for learning and demonstrating Playwright fundamentals.

---

## Features
- Homepage smoke test
- Navigation test using "Get started" and "Star" buttons
- Multi-tab/browser context test
- Mobile emulation test
- Page Object Model structure
- Testing for debugging purposes when creating tests

---

## Tech Stack
- Python
- pytest
- pytest-playwright
- black
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

## Additional Playwright features demonstrated
- API mocking with `page.route(...)`
- Full mocked JSON responses with `route.fulfill(...)`
- Modified live API responses with `route.fetch()` + `route.fulfill(...)`
- UI validation against intercepted network data

---

## Run locally
```bash
pip install -r requirements.txt
playwright install
python -m pytest -v
