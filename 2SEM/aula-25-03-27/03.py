import json

try:
    with open('dados.json') as arquivo:
        dados = json.load(arquivo)
        print('Consegui dar load no JSON.')
except FileNotFoundError as erro:
    print('O arquivo nao foi encontrado')
    print(f'Erro gerado: {erro}')
except Exception as exception:
    print('O arquivo foi encontrado, mas algum outro erro ocorreu')
    print(f'O erro encontrado foi {exception}')

print('Termino do programa')