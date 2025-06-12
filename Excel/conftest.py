import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones_excel import Funciones_Globales
url = "https://demoqa.com/text-box"

@pytest.fixture(scope="function")
def set_up_excel(playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1900, "height": 800},
        # record_video_dir="videos/Excel"
    )
    # Inicia Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(2000)

    yield page

    # Cerrar Context u Browser
    context.tracing.stop(path="trace.zip")
    context.close() 
    browser.close()