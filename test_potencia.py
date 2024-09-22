import pytest 
from Calculadora import potencia

def test_potencia_positivo():
    assert potencia(2, 3) == 8

def test_potencia_zero():
    assert potencia(2, 0) == 1

def test_potencia_base_um():
    assert potencia(1, 10) == 1

def test_potencia_base_zero():
    assert potencia(0, 3) == 0

def test_potencia_negativo():
    with pytest.raises(ValueError):
        potencia(2, -3)