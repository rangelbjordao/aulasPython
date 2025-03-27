from math import sqrt

'''
Em vez de levantar uma Exception generica, eu posso criar um tipo especifico de Exception que faca sentido na minha biblioteca ou aplicacao.

Nesse caso, estou criando uma classe EquacaoSemSolucao que é do tipo Exception. Portanto se comporta como Exception mas tem um nome especifico.
'''
class EquacaoSemSolucao(Exception):
    pass # essa classe (tipo) do tipo Execeptiton nao tem nada, só criei como uma subClasse de Exception

def resolve_eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        raise EquacaoSemSolucao('Essa equacao nao tem solucoes reais. Delta < 0.')

    x_1 = (-b + sqrt(delta))/2*a
    x_2 = (-b - sqrt(delta))/2*a

    return x_1, x_2

# equacao x**2 - 4 = 0
# a = 1, b= 0, c = -4 
solucao_1, solucao_2 = resolve_eq_seg_grau(1, 0, -4)
print(f'Solucoes: {solucao_1} e {solucao_2}')

solucao_1, solucao_2 = resolve_eq_seg_grau(1, 0, 4)
print(f'Solucoes: {solucao_1} e {solucao_2}')