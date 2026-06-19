from playwright.sync_api import Playwright, expect


def test_homepage_on_iphone_13(new_context, playwright: Playwright, tmp_path):
    iphone_13 = playwright.devices["iPhone 13"]
    context = new_context(**iphone_13)
    page = context.new_page()

    page.goto("https://playwright.dev/")
    expect(page.get_by_role("link", name="Get started")).to_be_visible()

    screenshot_file = tmp_path / "homepage-iphone13.png"
    page.screenshot(path=str(screenshot_file), full_page=True)

    context.close()