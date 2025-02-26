arquivo = open('meu_arquivo.txt', 'a')

arquivo.write('Esta linha foi adicionada por um programa.\n')

# boa praticao: fechar o arquivo apos o uso
arquivo.close()