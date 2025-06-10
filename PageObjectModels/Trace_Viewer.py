#Se ejecuta de forma normal generando archivo .zip
#-playwright show-trace trace_viewer.zip

# Para entrar en modo debug inplementar comando: 
# - set PWDEBUG=1 // para terminar Debug cambiar a 0

import re
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

ruta = "Evidencias/"
numA = random.sample(range(1,4),1)
nomA =random.sample(range(1,1000),4)
Pagina_Prueba = "https://demoqa.com/automation-practice-form"
rutaArchivos = "C:/Practicas/Playwright/Playwright/PageObjectModels/Pdf/EXPLODE - Manual de Desactivación TEIA.pdf"

def test_trace_viewer(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        viewport={"width": 1280, "height": 1080},
        # record_video_dir="videos/TraceViewer"
    )

    # Inicia Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto(Pagina_Prueba)
    page.set_default_timeout(2000)

    F = Funciones_Globales(page)
    expect(page).to_have_title("DEMOQA")  # Verificar que el título de la página sea "DEMOQA"  
    
    # Aquí se pueden agregar más interacciones con la página
    # utilizando los métodos de la clase Funciones_Globales
    
    F.Esperar()
    F.Scroll(0, 300)   

    #Iniciar Debug
    #page.pause()      

    F.TextoEvidencia("#firstName", "Santiago" + str(nomA[0]), ruta+"Nombre.png")
    F.Texto(f"#lastName", "Villanueva"+ str(nomA[0]))     
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
    F.Cargar_archivo("#uploadPicture", rutaArchivos)  # Cargar un archivo

    F.TomarScreenchot(ruta+"FormularioCompleto.png")  # Tomar screenshot del formulario completo
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
    
    F.Esperar(5)  # Esperar 2 segundos para que se procese el formulario

    # Detener Trace Viewer y guardar el archivo de trazas
    context.tracing.stop(path="trace_viewer.zip")

    # Cerrar Context u Browser
    context.close()   
    browser.close()