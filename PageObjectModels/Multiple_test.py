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

#@pytest.mark.skip(reason="Skipping test_select for example")
def test_select(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
            viewport={"width": 1280, "height": 1080},
            #record_video_dir="videos/Select"
    )               
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.set_default_timeout(2000)
    

    F= Funciones_Globales(page)
    expect(page).to_have_title("DEMOQA")
    F.Esperar()
    F.Scroll(0, 300)         

    F.Texto("#firstName", "Santiago" + str(nomA[0]))
    F.Texto(f"#lastName", "Villanueva"+ str(nomA[0]))     
    F.Texto("#userEmail", "fire@dsfsdf.com")
    F.Click("//label[contains(text(),'Male')]")
    F.Texto("#userNumber", "1234567890")
    #F.Fecha("#dateOfBirthInput","04 Jun 2025")  #Fecha con formato de texto
    F.FechaClick("#dateOfBirthInput", "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]")  #Fecha con click en el calendario
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press("Tab") # Ingresar un texto en el campo de materias
    F.Scroll(0, 400)
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

    # Cerrar Context u Browser
    context.close()   
    browser.close()
#@pytest.mark.xfail(reason="Skipping test_lista_dinamica for example XPASS")
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
    F.Texto("//input[@aria-controls='i0']", 'Ferra',1)
    F.Click_first('text=Ferrari', 2)
    F.Esperar(1) 

    context.close()  
    browser.close() 

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

    F.Esperar(1)
    F.Scroll(0, 300) 

    # Cerrar Context u Browser
    context.close()   
    browser.close() 