print("Qual o seculo?")

sec = int(input())

ano_final = sec*100
ano_inicial = ano_final - 99

print("este seculo vai do ano", ano_inicial, "ate o ano", ano_final)

if sec == 21:
    print("Este eo seculo atual")
else:
    print("Este nao e o seculo atual")