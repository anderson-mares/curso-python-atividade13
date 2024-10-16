# calculos.py

def potencia(base, expoente):
    """Calcula a potência de um número."""
    return base ** expoente

def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número."""
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return numero ** 0.5
