# obs: se eu nao especificar o modo de acesso, é suposto 'r' (apenas)

arquivo = open('texto.txt')

# readlines()
linhas = arquivo. readlines()

print(linhas)
print('A lista contem', len(linhas)), 'elementos'
print('(portanto esse é o numero de linhas no arquivo lido)')

''' Exercicio: contar apenas linhas que nao sao linhas em branco

Dica: fazer algo mais ao estilo do exemplo6.py
'''

arquivo.close()