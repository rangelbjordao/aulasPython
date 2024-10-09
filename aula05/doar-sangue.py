import datetime

data = datetime.datetime.now()
ano_atual = data.year

print("Em que ano voce nasceu?")
ano_nascimento = int(input())
idade = ano_atual - ano_nascimento

print("Estamos no ano", ano_atual)
print("Portanto voce fez ou fara", idade, "anos neste ano")

if(idade >= 18 and idade <= 59):
    print("Pode doar sangue")
elif(idade == 16 or idade ==17):
    print("Pode doar sangue se tiver autorização dos pais")
elif(idade >= 60 and idade <=69):
        print("Pode doar sangue contanto que seja doador já registrado.")
else:
    print("Nao é possível pode doar sangue com essa idade")
    
    
'''
Exercício para sexta - feira:
    
    * Pegar os campos "month" e "day" da data atual
    * Perguntar o dia e mes de nascimento do usuário
    * Descobrir se a pessoa ja fez aniversario esse ano e printar uma mensagem de acordo
'''