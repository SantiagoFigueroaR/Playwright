import re
from playwright.sync_api import Page, expect, BrowserContext, Playwright, sync_playwright
from funciones import Funciones_Globales

# playwright codegen https://www.saucedemo.com/
ruta = "Evidencias/"
rutaArchivos = "C:/Practicas/Playwright/Playwright/PageObjectModels/Pdf/EXPLODE - Manual de Desactivación TEIA.pdf"

def test_generator(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        # record_video_dir="videos/Generator" 
    )

    # Inicia Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(2000)

    F = Funciones_Globales(page)
    expect(page).to_have_title("Swag Labs")  # Verificar que el título de la página sea "DEMOQA"  

#Codigo generado por Playwright Codegen

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    F.Esperar()
    F.Scroll(0, 300) 