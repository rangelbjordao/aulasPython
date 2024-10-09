frutas = ["banana", "maca", "uva", "pera", "manga"]
legumes = ["abobora", "berinjela", "chuchu"]

compras = []
print("Escolha uma fruta. As opções são:")
print(frutas)

fruta_escolhida = input()

if fruta_escolhida in frutas:
    compras.append(fruta_escolhida)
    print(fruta_escolhida, "foi adicionada a lista de compras!")
    print(compras)
else:
    print(fruta_escolhida, "indisponivel: nao adicionei nada ao carrinho de compras")
    
'''
Exercicio:
* faca o mesmo com os legumes: apresente as opcoes e peca para o usuario escolher uma delas, adicionando ao carrinho (lista compras) se disponivel;

* crie uma terceira

'''