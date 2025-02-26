frutas = ["banana", "maça", "uva", "pera", "manga"]

carrinho = []

print("As opcoes de frutas sao:", *frutas)
print("Quantas frutas voce quer escolher?")

quantidade_frutas = int(input())
frutas_escolhidas = 0

while frutas_escolhidas < quantidade_frutas:
    print("Digite proxima fruta:")
    fruta = input()
    
    if fruta in frutas:
        carrinho.append(fruta)
        frutas_escolhidas += 1
    else:
        print(fruta, "indisponivel.")
    
print()
print("Carrinho de compras contem:")
print(*carrinho)