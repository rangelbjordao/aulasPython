'''
Este programa le um inteiro N e imprime todos os numeros pares de 0 ate N.
'''

N = int(input("Digite um numero inteiro:"))

for i in range(0, N+1, 2):
    print(i)