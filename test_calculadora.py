import pytest
from calculadora import sumar, restar, multiplicar, dividir

# Pruebas de Suma
def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

# Pruebas de Resta (Requisito: al menos dos pruebas)
def test_restar_positivos():
    assert restar(10, 4) == 6

def test_restar_resultado_negativo():
    assert restar(3, 8) == -5

# Pruebas de Multiplicación (Requisito: probar valores negativos)
def test_multiplicar_positivos():
    assert multiplicar(4, 5) == 20

def test_multiplicar_con_negativo():
    assert multiplicar(-3, 4) == -12

# Pruebas de División
def test_dividir_exactamente():
    assert dividir(10, 2) == 5

def test_dividir_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_cero_entre_numero(): # Requisito: cero entre un número distinto de cero
    assert dividir(0, 5) == 0

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

# Prueba de Validación (Requisito: entradas no numéricas)
def test_dividir_entradas_no_numericas():
    with pytest.raises(TypeError):
        dividir("diez", 2)