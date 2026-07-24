from pytest_playwright.pytest_playwright import page
from pages.home_page import HomePage
import pytest


@pytest.mark.smoke
def test_star_button_exists_on_homepage(page):
    """Verifies the Star button is visible on the homepage."""
    home = HomePage(page)
    home.goto()
    home.assert_star_button_exists()


@pytest.mark.regression
def test_star_button_links_to_github(page):
    """Verifies the Star button links to Playwright's GitHub repo."""
    home = HomePage(page)
    home.goto()

    href = home.page.locator(
        'a[href*="github.com/microsoft/playwright"]'
    ).first.get_attribute("href")
    assert href == "https://github.com/microsoft/playwright"
