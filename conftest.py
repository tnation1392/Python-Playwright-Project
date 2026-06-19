# conftest.py
import pytest
from pages.home_page import HomePage


@pytest.fixture
def base_url():
    return "https://playwright.dev/"


@pytest.fixture
def home_page(page, base_url):
    page.goto(base_url)
    return HomePage(page)