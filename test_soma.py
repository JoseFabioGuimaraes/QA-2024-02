import pytest 
from Calculadora import soma

def test_soma():
    assert soma(2,3) == 5

def test_soma_negativo():
    assert soma(-2,3) == 1

def test_soma_negativo_negativo():
    assert soma(-2,-3) == -5

def test_soma_numeros_reais():
    assert soma(2.5,3.5) == 6.0

