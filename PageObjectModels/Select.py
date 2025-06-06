import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

ruta = "Evidencias/"

def test_select(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="videos/Select"
    )               
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.set_default_timeout(2000)

    F= Funciones_Globales(page)
    F.Esperar()
    F.Scroll(0, 300)         

    F.TextoEvidencia("#firstName", "Santiago", ruta+"Nombre.png")
    F.Texto("#lastName", "Villanueva")     
    F.Texto("#userEmail", "fire@dsfsdf.com")
    F.Click("//label[contains(text(),'Male')]")
    F.Texto("#userNumber", "1234567890")
    #F.Fecha("#dateOfBirthInput","04 Jun 2025")  #Fecha con formato de texto
    F.FechaClick("#dateOfBirthInput", "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[3]")  #Fecha con click en el calendario
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press("Tab") # Ingresar un texto en el campo de materias
    # Elementos CheckBox
    for i in range(1,4):
        #print(i)
        page.locator(f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/label[1]").click()

    expect(page).to_have_url(re.compile(".*automation-practice-form"))
    
    F.Combo("//*[@id='state']/div/div[1]", 'NCR')  # Seleccionar un estado     
    F.Combo("//*[@id='city']", "Gurgaon")  # Seleccionar una ciudad
    page.keyboard.press("Tab") 

    F.TomarScreenchot(ruta+"FormularioCompleto.png")  # Tomar screenshot del formulario completo

    page.keyboard.press("Enter")
    
    F.Esperar(5)  # Esperar 2 segundos para que se procese el formulario


    # Cerrar Context u Browser
    context.close()   
    browser.close()