import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

def test_select(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(
                viewport={"width": 1920, "height": 1080, "PositionX": 100, "PositionY": 100},
        )               
        page = context.new_page()
        page.goto("https://demoqa.com/automation-practice-form")
        page.set_default_timeout(1000)

        F= Funciones_Globales(page)
        F.Esperar()
        F.Scroll(0, 200)         

        F.Texto("#firstName", "Santiago")
        F.Texto("#lastName", "Villanueva")     
        F.Texto("#userEmail", "fire@dsfsdf.com")
        F.Click("//label[contains(text(),'Male')]")
        F.Texto("#userNumber", "1234567890")
        F.Da
        

        # Cerrar Context u Browser
        context.close()   
        browser.close()