def soma(lista):
    s = 0
    for valor in lista:
        s = s + valor
    return s

def produto(lista):
    p = 1
    for valor in lista:
        p = p * valor
    return p

valores = [3, 8, -1, 5, 12, 0, 2]

print(produto(valores))

def media(x, y):
    return (x + y) / 2

def media_lista(lista):
    soma_elementos = soma(lista)
    quantidade_elementos = len(lista)
    return soma_elementos / quantidade_elementos