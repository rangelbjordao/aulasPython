import json

try:
    with open('dados.json') as arquivo:
        dados = json.load(arquivo)
        print('Consegui dar load no JSON.')
except FileNotFoundError:
    print('O arquivo nao foi encontrado')
except:
    print('O arquivo foi encontrado, mas algum outro erro ocorreu')

print('Termino do programa')