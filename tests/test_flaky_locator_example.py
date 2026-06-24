from playwright.sync_api import Page, expect


def test_locators_page_heading_flaky(page: Page) -> None:
    page.goto("https://playwright.dev/python/docs/locators")

    # ❌ BAD locator (too broad)
    heading = page.get_by_role("heading", name="Locators")

    # This may fail because multiple headings match
    expect(heading).to_be_visible()

    #Replace with this locator
def test_locators_page_heading_fixed(page: Page) -> None:
    page.goto("https://playwright.dev/python/docs/locators")

    # ✅ GOOD locator (specific + scoped)
    heading = page.get_by_role(
        "heading",
        name="Locators",
        exact=True
    )

    expect(heading).to_be_visible()