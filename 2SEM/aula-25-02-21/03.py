'''
Recebe um numero n e devole True, se é numero primo; False caso contrario
'''


def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, n, 2):
        if (n % i == 0):
            return False
    return True

'''
Mostra os numeros primos em um intervalo numerico
'''

'''
Vamos procurar primos maiores.
Comecando por volta de 1 Milhao
'''

inicio = 1000000
fim = inicio + 100
for i in range(inicio, fim):
    if primo(i):
        print(i)

inicio = int(1e7)  # 1*10^7 (10 milhoes)
fim = inicio + 100
for i in range(inicio, fim):
    if primo(i):
        print(i)

'''
Exercicio:

    (a) Execute um for como os acima para o intervalo comecando em 20 milhoes
    (b) Observe o tempo de execucao (a olho nu, o tempo que demora para printrar)
    (c) Defina uma funcao que recebe "inicio" e "fim" e realiza um for como os acima
'''

inicio = int(2e7)  # 2*10^7 (10 milhoes)
fim = inicio + 100
for i in range(inicio, fim):
    if primo(i):
        print(i)

# (b) fizemos