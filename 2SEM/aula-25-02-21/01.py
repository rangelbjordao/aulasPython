'''
numeros pares de 0 ate N
'''

print('Digite um inteiro positivo.')
N = int(input())

'''
i = 0
while i <= N:
'''

for i in range(0, N+1, 2):
    print(i)