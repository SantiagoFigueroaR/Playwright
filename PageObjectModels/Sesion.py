import random
import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

def test_sesion(set_up) -> None:
    page = set_up
    funciones = Funciones_Globales(page)
    expect(page).to_have_title("Swag Labs")

# def test_sesion2(set_up) -> None:
#     page = set_up
#     F = Funciones_Globales(page) 

#     F.Click("//*[@id='add-to-cart-sauce-labs-backpack']")
#     F.Click("#add-to-cart-sauce-labs-bolt-t-shirt")

#     expect(page).to_have_url(re.compile(".*/inventory.html"))

# def test_sesion3(set_up) -> None:
#     page = set_up
#     F = Funciones_Globales(page)

#     F.Click("#react-burger-menu-btn")
#     F.Click("#about_sidebar_link")

#     expect(page).to_have_url("https://saucelabs.com/")

def test_sesion4(set_up_validaNombre) -> None:
    page = set_up_validaNombre
    F = Funciones_Globales(page)
    txt = "Epic sadface: Username and password do not match any user in this service"
    F.Valida_Texto("//*[@id='login_button_container']/div/form/div[3]/h3",txt )

def test_sesion5(set_up_validaPassword) -> None:
    page = set_up_validaPassword
    F = Funciones_Globales(page)
    txt1 = "Epic sadface: Username and password do not match any user in this service"
    F.Valida_Texto("//*[@id='login_button_container']/div/form/div[3]/h3",txt1 )
