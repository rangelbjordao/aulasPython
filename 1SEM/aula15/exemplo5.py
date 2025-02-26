# Escreva um programa que permita ao usuario digitar quantos numeros quiser
# Os numeros serao salvos em uma lista

numeros = []

print("Quantos numeros quer digitar?")
quantidade_numeros = int(input())
numeros_digitados = 0

for numero_digitados in range(quantidade_numeros):
    print("Digite um numero:")
    numero = int(input())
    numeros.append(numero)
    numeros_digitados += 1

print
print("Numeros lidos:", numeros)

print("Maior", max(numeros))
print("Menor", min(numeros))
print("Total", sum(numeros))
print("Valor medio dos elementos", sum(numeros)/quantidade_numeros)

'''
Mostrar:
- Maior elemento da lista
- Menor elemento da lista
- Soma dos elementos da lista
'''
