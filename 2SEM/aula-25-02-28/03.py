temperaturas = []

with open('dados.txt') as arquivo:
    for linha in arquivo:
        temperaturas.append(float(linha))

'''
Exercício: crie (usando compreensão de lista):
    (a) temperaturas_altas, contendo as temperaturas acima de 90

    (b) temperaturas_muito_altas, contendo as temperaturas acima de 100

Depois vamos ver o tamanho dessas listas comparadas com a lista total
de temperaturas, para ver qual proporção do tempo está em temperatura alta
'''

temperaturas_altas = []
for temperatura in temperaturas:
    if temperatura >= 90 and temperatura < 100:
        temperaturas_altas.append(temperatura)
print(temperaturas_altas)
print('')

temperaturas_muito_altas = []
for temperatura in temperaturas:
    if temperatura >= 100:
        temperaturas_muito_altas.append(temperatura)
print(temperaturas_muito_altas)
print('')

temperaturas_altas = [
    temperatura for temperatura in temperaturas if temperatura >= 90 and temperatura < 100]
print(temperaturas_altas)
print('')

temperaturas_muito_altas = [
    temperatura for temperatura in temperaturas if temperatura >= 100]
print(temperaturas_muito_altas)
print('')

numero_temperaturas_altas = len(temperaturas_altas)
numero_temperaturas = len(temperaturas)
print('Proporcao do tempo em alta temperatura:', numero_temperaturas_altas / numero_temperaturas)