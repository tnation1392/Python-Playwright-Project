import pytest
from pages.home_page import HomePage


@pytest.fixture
def home_page(page, base_url):
    assert base_url, "base_url is empty. Set [pytest] base_url = https://playwright.dev in pytest.ini"
    page.goto(base_url)
    return HomePage(page)