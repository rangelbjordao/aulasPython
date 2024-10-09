import datetime

data = datetime.datetime.now()
ano_atual = data.year
mes_atual = data.month
dia_atual = data.day

print("Em que ano voce nasceu?")
ano_nascimento = int(input())

print("Qual o mes do seu aniversario? (1-12)")
mes_aniversario = int(input())

print("Qual o dia do seu aniversario? (1-31)")
dia_aniversario = int(input())

idade_maxima = ano_atual - ano_nascimento

if mes_aniversario <= mes_atual and dia_aniversario <= dia_atual:
    print("Voce ja fez aniversario", idade_maxima)
else:
    idade_maxima -= 1
    print("Voce ainda nao fez aniversario", idade_maxima)