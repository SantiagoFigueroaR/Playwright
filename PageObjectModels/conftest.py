import random
import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

rutaArchivos = "C:/Practicas/Playwright/Playwright/PageObjectModels/Pdf/EXPLODE - Manual de Desactivación T..-EIA.pdf"
Pagina_Prueba = "https://www.youtube.com/"

@pytest.fixture(scope="function")
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        # record_video_dir="videos/Select"
    )
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.set_default_timeout(2000)

    yield page

    context.close()
    browser.close()