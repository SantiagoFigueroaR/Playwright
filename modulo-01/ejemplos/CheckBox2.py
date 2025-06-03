#playwright codegen https://demoqa.com/checkbox

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_CheckBox2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo = 1000)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/CheckBox2"
    )
    page = context.new_page()

    
    page.goto("https://demoqa.com/checkbox")
    page.get_by_role("button", name="Toggle").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Notes").get_by_role("img").first.click()
    page.locator("label").filter(has_text="Commands").locator("path").first.click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^WorkSpace$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Angular").get_by_role("img").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_CheckBox2(playwright)
