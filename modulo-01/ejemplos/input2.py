import re
from playwright.sync_api import Page, expect,Playwright, sync_playwright

#def test_imput2(page: Page):
def test_imput2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo= 1000) #headless=True para no mostrar el navegador
    context = browser.new_context() 
    context =   browser.new_context(record_video_dir="videos/", record_video_size={"width": 1280, "height": 720}) #Grabar video de la prueba
    #page.set_viewport_size({"width": 1920, "height": 1080}) #Establecer el tamaño de la ventana del navegador
    
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/index.html") 
    expect(page).to_have_title("Formulario de Ejemplo")

    #Tiempo de esepera
    page.set_default_timeout(5000) #5 segundos

    page.locator("#nombre").fill("Santiago")
    page.locator("#apellidos").fill("Figueroa")
    page.locator("#tel").fill("5611111111")
    page.locator("#email").fill("fire@sdfgds.com")
    page.locator("#direccion").fill("lemontier 123")

    #Validar que el  boton este disponible
    boton_enviar = page.is_visible("//button[contains(text(),'Envia')]")
    print(boton_enviar)

    if boton_enviar:
        print("El botón 'Enviar' está visible.")
        page.locator("//button[contains(text(),'Enviar')]").click()        

    else:
        print("El botón 'Enviar' no está visible.")
        page.screenshot(path="Evidencia/boton_enviar_no_visible.png")
    page.screenshot(path="Evidencia/boton_enviar_click.png")    

    expect(page).to_have_url(re.compile(".*index.html"))
    
    context.close()
    browser.close()


    