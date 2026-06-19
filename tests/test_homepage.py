from pages.home_page import HomePage


def test_homepage_loads(page):
    home = HomePage(page)
    home.goto()
    home.assert_loaded()