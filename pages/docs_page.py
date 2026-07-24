from playwright.sync_api import Page, expect


class DocsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.installation_heading = page.get_by_role("heading", name="Installation")
        self.locators_heading = page.get_by_role("heading", name="Locators", exact=True)

    def assert_installation_visible(self) -> None:
        expect(self.installation_heading).to_be_visible()

    def assert_locators_page(self):
        expect(self.locators_heading).to_be_visible()
