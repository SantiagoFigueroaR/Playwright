import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_checkbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)  # headless=True para no mostrar el navegador
    context = browser.new_context()
    context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 1920, "height": 1080})  # Grabar video de la prueba
    

    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://demoqa.com/checkbox") 
    expect(page).to_have_title("DEMOQA")

    # check1 = page.locator("//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[1]").click()
    # check2 = page.locator("//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]/button[1]/*[1]").click()
    # check3 = page.locator("//body/div[@id='app']/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[1]/ol[1]/li[2]/span[1]/label[1]/span[1]/*[1]").click()

    page.locator("[aria-label='Toggle'] >> nth=0").click()  # Click en el primer checkbox
    page.locator("[aria-label='Toggle'] >> nth=1").click()  # Click en el segundo checkbox
    page.locator("text =Notes").click()

    #Cerrrar context y navegador
    context.close()

    browser.close()