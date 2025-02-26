# obs.: se eu não espeficiar o modo de acesso, é suposto "r" (apenas leitura)
arquivo = open('texto.txt')

# readlines() fornece o conteúdo do arquivo na forma de
# uma lista de linhas
linhas = arquivo.readlines()

# a linha a seguir imprime o conteúdo do arquivo no formato de lista de linhas
print(linhas)

linhas_em_branco = 0
for linha in linhas:
    if linha == '\n':
        linhas_em_branco += 1

print('Total de linhas:', len(linhas))
print('Número de linhas em branco:', linhas_em_branco)
print('Linhas que não são em branco:', len(linhas) - linhas_em_branco)

arquivo.close()
