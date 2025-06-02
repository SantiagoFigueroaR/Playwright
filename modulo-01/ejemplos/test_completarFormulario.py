import re
from playwright.sync_api import Page, expect

#Para ejecutar este test, se debe ejecutar el comando:
# pytest --slowmo=1500 --headed test_completarFormulario.py

def test_completar_formulario(page: Page, ):
    page.set_viewport_size({"width": 1920, "height": 1080}) #Establecer el tamaño de la ventana del navegador
    page.goto("https://demoqa.com/") 
    expect(page).to_have_title("DEMOQA")

    #Boton Elementos
    page.locator("text=Elements").click()
    page.screenshot(path="Evidencia/boton_Elementos_click.png")

    #Validar Url
    expect(page).to_have_url(re.compile(".*elements"))

    page.locator("text=Text Box").click()
    page.screenshot(path="Evidencia/boton_TextBox_click.png")
    expect(page).to_have_url(re.compile(".*text-box"))

    #Completar el formulario
    page.locator("#userName").fill("Santiago")
    page.screenshot(path="Evidencia/usuario_completado.png")

    page.locator("#userEmail").fill("eduardo.figueroa@teia.mx")
    page.screenshot(path="Evidencia/email_completado.png")

    page.locator("#currentAddress").fill("Calle 123")
    page.screenshot(path="Evidencia/direccion_actual_completada.png") 

    page.locator("#permanentAddress").fill("Calle 456")
    page.screenshot(path="Evidencia/direccion_permanente_completada.png")       

    #Enviar el formulario
    page.locator("#submit").click() 
    page.screenshot(path="Evidencia/boton_enviar_click.png")

    expect(page).to_have_url(re.compile(".*text-box"))
