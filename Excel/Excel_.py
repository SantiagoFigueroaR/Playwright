import re
import pytest
import openpyxl
from playwright.sync_api import Page, expect, sync_playwright

# intalar la siguiente libreria openpyxl:  pip install openpyxl

ruta_Excel = "C:/Practicas/Playwright/Playwright/Excel/datos_prueba.xlsx"
registros = 15

archivo = openpyxl.load_workbook(ruta_Excel)
def NumeroFilas(hoja):
    ac = archivo[hoja]
    return ac.max_row

def DatosColumna(hoja,fila,col):
    ac = archivo[hoja]
    col = ac.cell(int(fila),int(col))
    return col.value

print("Numero de filas: ", NumeroFilas("Hoja1"))
print("Datos de la columna 1, fila 2: ", DatosColumna("Hoja1",12,1))