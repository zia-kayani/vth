import pytest
from playwright.sync_api import sync_playwright

def test_getTitle():
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com')
        assert "Google" in page.title()
        browser.close()