def mostra_menu():
    print('Escolha uma das opções a seguir:')
    print('A - cadastrar nome')
    print('B - cadastrar idade')
    print('C - sair do programa')
    
# Node é um valor especial do Python para indicar ausência de dado
nome = None
idade = None
continua = True
while continua:
    mostra_menu()
    opcao = input()
    if opcao == 'A':
        nome = input('Digite o nome: ')
    elif opcao == 'B':
        idade = int(input('Digite a idade: '))
    elif opcao == 'C':
        continua = False
    else:
        print('Opção invalida.')
        
print('Programa esta encerrando.')
print('Nome cadastrado:', nome)
print('Idade cadastrada:', idade)