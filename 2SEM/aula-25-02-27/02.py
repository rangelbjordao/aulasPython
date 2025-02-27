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
Mostra os numeros primos em um intervalo
'''


def mostra_primos(inicio, fim):
    for i in range(inicio, fim):
        if primo(i):
            print(i)


# 1 milhoes até 10 milhoes e 100
# mostra_primos(1000000, 1000100)

# 10 milhoes até 10 milhoes e 100
# mostra_primos(int(1e7), int(1e7) + 100)

# 20 milhoes até 10 milhoes e 100
# mostra_primos(int(2e7), int(2e7) + 100)

'''
Exercicio:

    (a) Altere a funcao para receber, em vez de inicio e fim do intervalo,
    receber o inicio e o TAMANHO do intervalo
'''


def mostra_primos(inicio, intervalo):
    intervalo = inicio + intervalo
    for i in range(inicio, intervalo):
        if primo(i):
            print(i)


mostra_primos(int(1e7), 100)
