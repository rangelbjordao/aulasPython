print("Qual o seu nome?")
nome = input()

print("Qual o seu sobrenome?")
sobrenome = input()

print("Ola ", nome, sobrenome)

print("Em que ano voce nasceu?")
ano_nascimento =  int(input())

idade = 2024 - ano_nascimento
print("Sua idade é no maximo: ", idade)

if (ano_nascimento <= 2000 and ano_nascimento >=1901) :
    print("Voce nasceu no seculo XX")
elif (ano_nascimento >= 2001 and ano_nascimento <= 2100):
    print("Voce nasceu no seculo XXI")
else:
    print("... serio?")