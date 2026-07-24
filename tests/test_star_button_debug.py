from pages.home_page import HomePage
import pytest


def test_inspect_star_button(page):
    """Debug: Print all links to find the Star button."""
    page.goto("https://playwright.dev/")

    # Get all links with text containing "star"
    all_links = page.get_by_role("link").all()

    print("\n=== All Links on Page ===")
    for i, link in enumerate(all_links):
        text = link.text_content().strip()
        href = link.get_attribute("href") or "no href"
        visible = link.is_visible()
        print(f"{i}: Text='{text}' | Href='{href}' | Visible={visible}")

    print("\n=== Links matching 'Star' ===")
    star_links = page.get_by_role("link", name="Star").all()
    for i, link in enumerate(star_links):
        text = link.text_content().strip()
        href = link.get_attribute("href") or "no href"
        print(f"{i}: Text='{text}' | Href='{href}'")
