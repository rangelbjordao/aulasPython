import json

NOME_ARQUIVO = 'pacientes.json'


def carrega_pacientes():
    with open(NOME_ARQUIVO) as arquivo:
        pacientes = json.load(arquivo)
    return pacientes


# recebe a lista de pacientes e escreve seus dados no arquivo JSON
def escreve_pacientes_no_arquivo(pacientes: list):
    # abro o arquivo no modo de escrita (Write, por isso o w)
    with open(NOME_ARQUIVO, 'w') as arquivo:
        json.dump(pacientes, arquivo, indent=4)


def mostra_nomes(pacientes: list):
    for paciente in pacientes:
        print('Nome: ', paciente['nome'])


def le_novo_paciente():
    paciente = {}

    print('Informe o nome do paciente:')
    nome = input()
    paciente['nome'] = nome

    print('Informe a idade do paciente:')
    idade = int(input())
    paciente['idade'] = idade

    print('Informe o id do paciente:')
    id = int(input())
    paciente['id'] = id

    return paciente


'''
Exercicio: escreva funcao que recebe lista de pacientes e printa todas as informacoes (nome, idade, id)
'''


def mostra_dados(pacientes: list):
    for paciente in pacientes:
        print('Nome: ', paciente['nome'])
        print('Idade: ', paciente['idade'])
        print('Id: ', paciente['id'])
        print()


def main():
    pacientes = carrega_pacientes()
    em_execucao = True

    while em_execucao:
        print('Escolha uma opcao:')
        print('0. Sair do programa')
        print('1. Mostrar pacientes')
        print('2. Cadastrar paciente')

        opcao = int(input())
        if opcao == 0:
            em_execucao = False
        elif opcao == 1:
            mostra_dados(pacientes)
        elif opcao == 2:
            novo_paciente = le_novo_paciente()
            pacientes.append(novo_paciente)

    escreve_pacientes_no_arquivo(pacientes)
    print('Base de dados atualizada com sucesso.')
    print("Terminando programa...")


main()
