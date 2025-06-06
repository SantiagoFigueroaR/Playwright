import re
from playwright.sync_api import Page, expect, Playwright, sync_playwright

def test_checkbox3(playwright : Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)  # headless=True para no mostrar el navegador
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/CheckBox3",
        record_video_size={"width": 1280, "height": 720}  # Grabar video de la prueba
    )
    page = context.new_page()
    
    page.goto("https://demoqa.com/automation-practice-form")
    expect(page).to_have_title("DEMOQA")
    page.set_default_timeout(5000)  # Establecer tiempo de espera por defecto a 5 segundos

    #Scroll de pagina
    page.mouse.wheel(0, 100) 

    page.locator("//input[@id='firstName']").fill("John Doe")
    page.locator("//input[@id='lastName']").fill("Smith")
    page.locator("//input[@id='userEmail']").fill("eduardo.figue@gmail.com")
    page.locator("//label[contains(text(),'Male')]").click()

    page.locator("//input[@id='userNumber']").fill("1234567890")
    page.locator("//input[@id='dateOfBirthInput']").fill("01 Jan 2000")
    page.keyboard.press("Enter")  # Presionar Enter para confirmar la fecha
    page.locator('#subjectsInput').fill('Matemáticas') 
    
    # Elementos CheckBox con check y uncheck

    # page.locator("//label[contains(text(),'Sports')]").check()
    # page.locator("//label[contains(text(),'Reading')]").check()
    # page.locator("//label[contains(text(),'Reading')]").uncheck()  
    # page.locator("//label[contains(text(),'Music')]").check()

    # CheckBox con ciclo for

    for i in range(1,4):
        #print(i)
        page.locator(f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/label[1]").click()

    expect(page).to_have_url(re.compile(".*automation-practice-form"))


    # Cerrar contexto y navegador
    context.close()
    browser.close()