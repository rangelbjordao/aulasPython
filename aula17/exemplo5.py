# 'r' significa abrir em modo leitura
arquivo = open('texto2.txt', 'r')

# outro jeito de acessar: em um for
# o arquivo e tratado como sequencia de linhas

totalLinhas = 0
totalBom = 0
for linha in arquivo:
    totalLinhas += 1
    linha = linha.strip()  # remove espacamentos adicionais
    if 'bom' in linha:
        totalBom += 1
# caractere \ (backslash ou escape) 
print('total de linhas', totalLinhas)
print('total de \"bom\"', totalBom)

''' Exercicio:
(a) Contar o numero de linhas existentes no arquivo
(b) Contar o numero de linhas que contem a palavra "bom"
'''

arquivo.close()
