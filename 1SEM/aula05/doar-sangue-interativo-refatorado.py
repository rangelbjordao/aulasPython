print("Qual sua idade?")
idade = int(input())

pode_doar = False # "flag" -- booleano (indica se algo é verdadeiro ou falso)

if idade >= 18 and idade <= 59:
    pode_doar = True
elif idade == 16 or idade == 17:
    print("Voce tem autorização dos pais? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S":
        pode_doar = True
elif idade >= 60 and idade <= 69:
    print("Voce ja doou sangue anteriormente? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S":
        pode_doar = True
        
if pode_doar: # estamos verificando se a variável vale true
    print("Voce pode doar sangue.")
else:
    print("Voce nao pode doar sangue.")