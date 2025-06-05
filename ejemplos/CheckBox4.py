import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_checkBox4(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(
                viewport={"width": 1920, "height": 1080},
        )
        page = context.new_page()
        
        page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
        expect(page).to_have_title(re.compile("DataTables example - No ordering"))
        page.set_default_timeout(2000)

        # scroll de la pagina 
        page.mouse.wheel(0, 300)

        for i in range(1, 11):
            # Check the checkbox
            page.locator(f"//*[@id='example']/tbody[1]/tr[{i}]/td[1]/input[1]").click()

            if i == 10:
                page.locator(f"//*[@id='example_wrapper']/div[3]/div[2]/div[1]/nav[1]/button[4]").click()
                for x in range(1, 11):
                    page.locator(f"//*[@id='example']/tbody[1]/tr[{x}]/td[1]/input[1]").click()
                    if x == 10:
                        page.locator(f"//*[@id='example_wrapper']/div[3]/div[2]/div[1]/nav[1]/button[5]").click()
                        for y in range(1, 11):
                            page.locator(f"//*[@id='example']/tbody[1]/tr[{y}]/td[1]/input[1]").click()
                        page.locator("//input[@id='dt-search-0']").fill("Je")
                        page.locator("//*[@id='example']/tbody[1]/tr[3]/td[1]/input[1]")..click()
            

        # Close the browser
        context.close()
        browser.close()
