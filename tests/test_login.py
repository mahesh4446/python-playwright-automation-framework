from pages.login_page import LoginPage
from pages.login_page import LoginPage


def test_login_page(page):
    login_page = LoginPage(page)

    login_page.open("https://the-internet.herokuapp.com/login")

    assert page.title() == "The Internet"


def test_login_page_elements(page):
    login_page = LoginPage(page)

    login_page.open("https://the-internet.herokuapp.com/login")

    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("button[type='submit']").is_visible()
