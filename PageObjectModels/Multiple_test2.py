import random
import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

ruta = "Evidencias/"
#Metodo Random 
numA = random.sample(range(1,4),1)
nomA =random.sample(range(1,1000),4)
rutaArchivos = "C:/Practicas/Playwright/Playwright/PageObjectModels/Pdf/EXPLODE - Manual de Desactivación TEIA.pdf"
Pagina_Prueba = "https://www.youtube.com/"


def test_select(set_up) -> None:
    page: Page = set_up
    F= Funciones_Globales(page)
    expect(page).to_have_title("DEMOQA")
    F.Esperar()
    F.Scroll(0, 300)         

    F.Texto("#firstName", "Santiago" + str(nomA[0]))
    F.Texto(f"#lastName", "Villanueva"+ str(nomA[0]))     
    F.Texto("#userEmail", "fire@dsfsdf.com")
    F.Click("//label[contains(text(),'Male')]")
    F.Scroll(0, 400) 
    F.Texto("#userNumber", "1234567890")
    F.FechaClick("#dateOfBirthInput", "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]")  #Fecha con click en el calendario
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press("Tab")
    # Elementos CheckBox
    for i in range(1,4):
        page.locator(f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/label[1]").click()

    expect(page).to_have_url(re.compile(".*automation-practice-form"))  
    F.Cargar_archivo("#uploadPicture", rutaArchivos)  # Cargar un archivo
    F.Combo("//*[@id='state']/div/div[1]", 'NCR')

    #Metodo Random 
    numA = random.sample(range(1,4),1)

    if numA[0] == 1:
        F.Combo("//*[@id='city']", "Delhi")
    elif numA[0] == 2:
        F.Combo("//*[@id='city']", "Gurgaon")
    elif numA[0] == 3:
        F.Combo("//*[@id='city']", "Noida")
    page.keyboard.press("Tab")

    page.keyboard.press("Enter")    
    F.Esperar(1)

def test_lista_dinamica(set_up) -> None:    
    page: Page = set_up
    F = Funciones_Globales(page)
    page.goto(Pagina_Prueba)

    page.set_default_timeout(5000)
    expect(page).to_have_title("YouTube") # Verificar que el título de la página sea "YouTube"
    
    F.Texto("//input[@aria-controls='i0']", 'Ferra',1)
    F.Click_first('text=Ferrari', 2)
    F.Esperar(1)  

def test_generator(set_up) -> None:   
    page: Page = set_up
    F = Funciones_Globales(page)
    page.goto("https://www.saucedemo.com/")  # Ir a la página de Swag Labs
    expect(page).to_have_title("Swag Labs")  # Verificar que el título de la página sea "DEMOQA"  

#Codigo generado por Playwright Codegen

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    F.Esperar(1)
    F.Scroll(0, 300) 