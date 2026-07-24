from playwright.sync_api import Page, Route, expect


def test_mock_fruit_api(page: Page) -> None:
    """Verifies that the mock_fruit_api function works correctly."""

    def handle_fruit_api(route: Route) -> None:
        """Handles the mock_fruit_api route."""
        mock_data = [
            {"name": "Strawberry", "id": 21},
            {"name": "Blueberry", "id": 22},
            {"name": "Blackberry", "id": 23},
        ]
        route.fulfill(status=200, json=mock_data)

    page.route("**/api/v1/fruits", handle_fruit_api)
    page.goto("https://demo.playwright.dev/api-mocking")

    expect(page.get_by_text("Strawberry", exact=True)).to_be_visible()
    expect(page.get_by_text("Blueberry", exact=True)).to_be_visible()
    expect(page.get_by_text("Blackberry", exact=True)).to_be_visible()
