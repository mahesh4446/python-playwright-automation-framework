
def test_example_page(page):
    page.goto("https://example.com")

    assert page.title() == "Example Domain"


def test_example_page_content(page):
    page.goto("https://example.com")

    heading = page.locator("h1").text_content()

    assert heading == "Example Domain"
