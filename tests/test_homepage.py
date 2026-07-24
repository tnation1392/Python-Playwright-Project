from pages.home_page import HomePage


def test_homepage_loads(page):
    """Verifies that the homepage loads."""
    home = HomePage(page)
    home.goto()
    home.assert_loaded()
