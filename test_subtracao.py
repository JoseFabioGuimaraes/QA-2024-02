import pytest 
from Calculadora import subtracao

def test_subtracao():
    assert subtracao(5,3) == 2

def test_subtracao_negativo():
    assert subtracao(-2,3) == -5

def test_subtracao_negativo_negativo():
    assert subtracao(-2,-3) == 1

def test_subtracao_numeros_reais():
    assert subtracao(2.5,3.5) == -1.0

def test_subtracao_zero():
    assert subtracao(5,0) == 5
