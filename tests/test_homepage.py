from pages.home_page import HomePage


def test_homepage_loads(home_page):
    home_page.assert_loaded()
