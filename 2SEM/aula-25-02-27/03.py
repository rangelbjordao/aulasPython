'''
Exercicio de organizacao de codigo:

Fazer um arquivo primo.py com a funcao primo, e dar import nesse arquivo em vez de precisar dar ctrl+c ctrl+v na funcao.
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


def mostra_primos(inicio, fim=None, tamanho=100):
    # se o fim nao for fornecido, calculo como sendo inicio + tamanho
    if fim is None:
        fim = inicio + tamanho
    for i in range(inicio, fim):
        if primo(i):
            print(i)

# nessa chamada, fica implicito que o 40 é o "fim" pois é o segundo parametro
mostra_primos(15, 40)

# preciso nomear o parametro "tamanho" senao seria suposto que 550 é o "fim"
mostra_primos(100, tamanho=50)

# pro clareza, é llegal usar parametros nomeados mesmo quando nao obrigatorio
mostra_primos(inicio=15, fim=40)
