from playwright.sync_api import Page, expect

def test_locators_page_heading_fixed(page: Page) -> None:
    page.goto("https://playwright.dev/python/docs/locators")

    # Good locator
    heading = page.get_by_role(
        "heading",
        name="Locators",
        exact=True
    )

    expect(heading).to_be_visible()