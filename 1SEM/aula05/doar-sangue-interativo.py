print("Qual sua idade?")
idade = int(input())

if idade >= 70 or idade < 16:
    print("Nao pode doar sangue")
elif idade == 16 or idade == 17:
    print("Voce tem autorização dos pais? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S":
        print("Pode doar sangue.")
    else:
        print("Nao pode doar sangue.")
elif idade >= 60 and idade <= 69:
        print("Voce ja doou sangue anteriormente? (S/N)")
        resposta = input()
        if resposta == "s" or resposta == "S":
            print("Pode doar sangue")
        else:
            print("Nao pode doar sangue")
else:
    print("Pode doar sangue.")