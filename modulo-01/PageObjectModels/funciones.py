import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

class Funciones_Globales:
    #iniciador de la clase Funciones_Globales
    def __init__(self, page: Page):
        self.page = page

    def Esperar(self, tiempo = 0.3):
        time.sleep(tiempo)

    def Scroll(self, x, y, tiempo = 0.3):
        self.page.mouse.wheel(x, y)
        self.Esperar(tiempo)

    def Texto(self, selector, texto, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        self.Esperar(tiempo)
    
    def Click(self, selector, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.Esperar(tiempo)
