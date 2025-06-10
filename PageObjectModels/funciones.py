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

    def TomarScreenchot(self, ruta, tiempo = 0.3):
        self.page.screenshot(path=ruta)
        self.Esperar(tiempo)

    def TextoEvidencia(self, selector, texto, ruta, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(texto)
        self.page.screenshot(path=ruta)
        self.Esperar(tiempo)
    
    def Click(self, selector, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.Esperar(tiempo)

    def Fecha(self, selector, fecha, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.fill(fecha)
        self.page.mouse.click(0, 50)    # Click para cerrar el calendario
        self.Esperar(tiempo)

    def FechaClick(self, selector, clickFecha, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        p = self.page.locator(clickFecha)
        expect(p).to_be_visible()
        expect(p).to_be_enabled()  
        p.highlight()
        p.click()        
        self.Esperar(tiempo)

    def Combo(self, selector, texto, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.Esperar(tiempo)
        opciones  = self.page.locator(f"//div[contains(text(),'{texto}')]", ) # Tienes que adecuar el selector según tu necesidad
        expect(opciones).to_be_visible()
        expect(opciones).to_be_enabled()
        opciones.highlight()
        opciones.click()
        self.Esperar(tiempo)

    def Combo_label(self, selector, texto, tiempo = 0.3):
        t = self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label = texto)
        self.Esperar(tiempo)

    def Cargar_archivo(self, selector, rutaArchivo, tiempo = 0.3):
        t = self.page.locator(selector).set_input_files(rutaArchivo)
        self.Esperar(tiempo)
        
    def Quitar_Archivo(self, selector, tiempo = 0.3):
        t = self.page.locator(selector).set_input_files([])
        self.Esperar(tiempo)

    def Click_first(self, selector, tiempo = 0.3):
        t = self.page.locator(selector).first.click()
        self.Esperar(tiempo)