import pytest
from playwright.sync_api import sync_playwright
from config.config import BROWSER, HEADLESS


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser_type = getattr(p, BROWSER)
        browser = browser_type.launch(headless=HEADLESS)

        page = browser.new_page()

        yield page

        browser.close()
