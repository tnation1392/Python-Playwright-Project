from pages.home_page import HomePage
from pages.docs_page import DocsPage


def test_get_started_navigates_to_installation(page):
    home = HomePage(page)
    docs = DocsPage(page)

    home.goto()
    home.click_get_started()
    docs.assert_installation_visible()