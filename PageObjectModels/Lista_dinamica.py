import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

Pagina_Prueba = "https://www.youtube.com/"

def test_lista_dinamica(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        #record_video_dir="videos/ListaDinamica"
    )
    page = context.new_page()
    page.goto(Pagina_Prueba)
    page.set_default_timeout(2000)

    F = Funciones_Globales(page)
    expect(page).to_have_title("YouTube") # Verificar que el título de la página sea "YouTube"
    F.Texto("//input[@aria-controls='i0']", 'Ferra',2)
    F.Click_first('text=Ferrari', 3)
    F.Esperar(5) 
    
    # Aquí se pueden agregar más interacciones con la página de prueba
    # utilizando los métodos de la clase Funciones_Globales

    context.close()  
    browser.close()  