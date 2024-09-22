def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def fatorial(a):
    if not isinstance(a, int):
        raise ValueError("O fatorial de um número não inteiro não existe")
    if (a < 0):
        raise ValueError("O fatorial de um número negativo não existe")
    elif (a == 0):
        return 1
    else:
        return a * fatorial(a-1)

def potencia(a,b):
    if (b < 0):
        raise ValueError("Potência negativa não existe")
    else:
        return a ** b
