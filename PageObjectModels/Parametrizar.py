import random
import re
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales


data = [("santiago", "fire@hasda.com","Calle2"),
        ("santi", "sdfdsf@sdfsdf.com","Calle3"),
        ("santi2", "santi2@hasda.com","Calle4")]

@pytest.mark.parametrize("nombre, email, direccion", data)
def test_parametrizar(set_up_parametros, nombre, email, direccion) -> None:
    page = set_up_parametros
    F = Funciones_Globales(page)

    expect(page).to_have_title("DEMOQA")

    F.Texto("#userName", nombre)
    F.Texto("#userEmail", email)   
    F.Texto("#currentAddress", direccion)