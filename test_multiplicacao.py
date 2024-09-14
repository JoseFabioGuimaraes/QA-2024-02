import pytest 
from Calculadora import multiplicacao

def test_multiplicacao():
    assert multiplicacao(2,3) == 6

def test_multiplicacao_negativo():
    assert multiplicacao(-2,3) == -6

def test_multiplicacao_negativo_negativo():
    assert multiplicacao(-2,-3) == 6

def test_multiplicacao_numeros_reais():
    assert multiplicacao(2.5,3.5) == 8.75

def test_multiplicacao_zero():
    assert multiplicacao(5,0) == 0

def test_multiplicacao_zero_nao_zero():
    assert not multiplicacao(5,0) == 5