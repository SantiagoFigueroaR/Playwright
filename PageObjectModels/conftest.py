import random
import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

rutaArchivos = "C:/Practicas/Playwright/Playwright/PageObjectModels/Pdf/EXPLODE - Manual de Desactivación T..-EIA.pdf"
Pagina_Prueba = "https://www.youtube.com/"
ruta = "https://saucedemo.com/"

@pytest.fixture(scope="function")
def set_upUno(playwright: Playwright) -> None:
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

@pytest.fixture(scope="session")
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        # record_video_dir="videos/Select"
    )
    #Inicia TraceViewer
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    page = context.new_page()
    page.goto(ruta)
    page.set_default_timeout(2000)
    expect(page).to_have_title("Swag Labs")
    
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    yield page

    context.tracing.stop(
        path="TraceSelect.zip"
    )

    context.close()
    browser.close()

@pytest.fixture(scope="session")
def set_up_validaNombre(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        # record_video_dir="videos/Select"
    )
    #Inicia TraceViewer
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    page = context.new_page()
    page.goto(ruta)
    page.set_default_timeout(2000)
    expect(page).to_have_title("Swag Labs")
    
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_userr")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    yield page

    context.tracing.stop(
        path="TraceSelect.zip"
    )

    context.close()
    browser.close()