import re
from playwright.sync_api import BrowserContext, expect
from pages.docs_page import DocsPage


def test_two_tabs_in_same_context(context: BrowserContext):
    """Verifies that two tabs exist in the same context."""
    home_tab = context.new_page()
    docs_tab = context.new_page()

    home_tab.goto("https://playwright.dev/")
    docs_tab.goto("https://playwright.dev/python/docs/locators")

    expect(home_tab).to_have_title(re.compile("Playwright"))

    docs = DocsPage(docs_tab)
    docs.assert_locators_page()

    assert len(context.pages) >= 2
