from playwright.sync_api import Page, expect


class DocsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.installation_heading = page.get_by_role(
            "heading", name="Installation"
        )

    def assert_installation_visible(self) -> None:
        expect(self.installation_heading).to_be_visible()