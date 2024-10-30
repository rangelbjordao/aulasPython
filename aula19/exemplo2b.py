'''
Esse programa vai abrir o arquivo de configuracao criado pelo programa exemplo2a.py

Estamos supondo que o arquivo config.txt ja existe e esta preenchido
'''

# obs: nao estamos verificando se o arquivo ja existe
arquivo_config = open('config.txt')

# abre arquivo como lista de linhas
linhas = arquivo_config.readlines()

if linhas == []:
    print('Arquivo de configuracao vazio. Encerrando')
    exit()

nome = linhas[0].strip() # strip() remove o \n no final
idade = int(linhas[1])
altura = float(linhas[2])

print('Ola,', nome)
print('Seus dados estao salvos.')
print('Sua idade é', idade)
print('Sua altura é', altura)