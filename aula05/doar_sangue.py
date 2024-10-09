print("Em que ano voce nasceu?")
ano_nascimento = int(input())

idade = 2024 - ano_nascimento

if(idade >= 18 and idade <= 60):
    print("Voce tem", idade, "anos e pode doar sangue")
elif(idade >= 16 and idade <=17):
    print("Voce tem", idade, "anos e pode doar sangue com autorizacao dos pais")
elif(idade >= 61 and idade <=69):
    print("Ja doou sangue anteriormente? s ou n (sim ou nao)")
    ja_doou = input()
    if(ja_doou == "sim" or "s"):
        print("Voce tem", idade, "anos e pode doar sangue pois ja doou anteriormente")
    elif(ja_doou == "nao" or "n"):
        print("Voce tem", idade, "anos e nao pode doar sangue por nao ter doado anteriormente")
    else:
        print("resposta invalida")
else:
    print("Voce tem", idade, "anos e nao pode doar sangue")