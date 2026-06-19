from playwright.sync_api import Page, Route, expect


def test_patch_fruit_api_response(page: Page) -> None:
    def handle_fruit_api(route: Route) -> None:
        response = route.fetch()
        fruits = response.json()
        fruits.append({"name": "Loquat", "id": 100})

        route.fulfill(
            response=response,
            json=fruits
        )

    page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", handle_fruit_api)
    page.goto("https://demo.playwright.dev/api-mocking")

    expect(page.get_by_text("Loquat", exact=True)).to_be_visible()
