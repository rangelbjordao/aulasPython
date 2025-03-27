'''
Esse programa GERA exceptions.
'''

from math import sqrt


def resolve_eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        raise Exception('Essa equacao nao tem solucoes reais. Delta < 0.')

    x_1 = (-b + sqrt(delta))/2*a
    x_2 = (-b - sqrt(delta))/2*a

    return x_1, x_2

# equacao x**2 - 4 = 0
# a = 1, b= 0, c = -4 
solucao_1, solucao_2 = resolve_eq_seg_grau(1, 0, -4)
print(f'Solucoes: {solucao_1} e {solucao_2}')

solucao_1, solucao_2 = resolve_eq_seg_grau(1, 0, 4)
print(f'Solucoes: {solucao_1} e {solucao_2}')