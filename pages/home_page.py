from playwright.sync_api import Page, expect
import re


class HomePage:
    URL = "https://playwright.dev/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.get_started_link = page.get_by_role("link", name="Get started")

    def goto(self) -> None:
        self.page.goto(self.URL)

    def assert_loaded(self) -> None:
        expect(self.page).to_have_title(re.compile("Playwright"))
        expect(self.get_started_link).to_be_visible()

    def click_get_started(self) -> None:
        self.get_started_link.click()