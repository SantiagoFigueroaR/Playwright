import re 
from playwright.sync_api import Page,expect

def test_uno(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

    boton_uno = page.locator("text=Get started")
    expect(boton_uno).to_have_attribute("href", re.compile("/docs/intro"))
    page.screenshot(path="Evidencia/Valida_Texto.png")
    boton_uno.click()

    #Tomar Evidencia de la accion realizada
    page.screenshot(path="Evidencia/Click_GetStarted.png")

    #Validar la ruta de pagina destino
    expect(page).to_have_url(re.compile(".*docs/intro"))  #.* sirve para indicar que puede haber cualquier cosa antes de "docs/intro"