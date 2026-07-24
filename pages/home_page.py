from playwright.sync_api import Page, expect
import re


class HomePage:
    URL = "https://playwright.dev/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.get_started_link = page.get_by_role("link", name="Get started")
        self.star_link = page.get_by_role("link", name="Star| Github")

    def goto(self) -> None:
        self.page.goto(self.URL)

    def assert_loaded(self) -> None:
        """Asserts that the page is loaded."""
        expect(self.page).to_have_title(re.compile("Playwright"))
        expect(self.get_started_link).to_be_visible()

    def click_get_started(self) -> None:
        """Clicks the Get started button to go to GitHub."""
        self.get_started_link.click()

    def assert_star_button_exists(self) -> None:
        """Validates the Star button (GitHub link) is present and visible."""
        star_button = self.page.locator(
            'a[href*="github.com/microsoft/playwright"]'
        ).first
        expect(star_button).to_be_visible()

    def click_star_button(self) -> None:
        """Click the Star button to go to GitHub."""
        star_button = self.page.locator(
            'a[href*="github.com/microsoft/playwright"]'
        ).first
        star_button.click()
