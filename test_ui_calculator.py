import os

from playwright.sync_api import sync_playwright

def test_ui_addition():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("file://" + os.path.abspath("calculator.html"))

        page.fill("#num1", "2")
        page.fill("#num2", "3")
        page.click("button")

        result = page.text_content("#result")
        assert float(result) == 5.0

        browser.close()