

def e_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print('Digite um inteiro positivo.')
N = int(input())

for i in range(N + 1):
    if e_par(i):
        print(i)