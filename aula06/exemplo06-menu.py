# Menu para cadastro de dados de doador de sangue

nome = "Nao consta"
tipo_sanguineo = "Nao consta"

continuar_programa = True

while continuar_programa:
    print("Escolha uma opcao:")
    print("A - cadastrar nome")
    print("B - cadastrar tipo sanguineo")
    print("C - encerrar programa")

    comando = input()

    if comando == "A" or comando == "a":
        print("Digite o nome:")
        nome = input()
    elif comando == "B" or comando == "b":
        print("Digite o tipo sanguineo:")
        tipo_sanguineo = input()
    elif comando == "C" or comando == "c":
        continuar_programa = False
        print("Programa encerrado")
    else:
        print("Comando nao reconhecido")

print("Informacoes do doador:")
print("Nome: ", nome)
print("Tipo sanguineo: ", tipo_sanguineo)
