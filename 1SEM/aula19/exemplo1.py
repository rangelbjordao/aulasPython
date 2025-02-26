nome_arquivo = 'livro.txt'
arquivo = open(nome_arquivo)

print('Abrimos o arquivo', nome_arquivo)
print('Digite o termo a ser buscado no arquivo:')
termo = input()

# vamos acessar o arquivo como uma lista de linhas
linhas = arquivo.readlines()

ocorrencias = 0
print('Linhas do arquivo', nome_arquivo, 'contendo', termo)
for linha in linhas:
    if termo in linha:  # se o termo buscado ocorre nessa linha
        ocorrencias += 1
        print(linha.strip())

print(ocorrencias)