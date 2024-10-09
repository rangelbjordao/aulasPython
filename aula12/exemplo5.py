texto1 = 'bom dia'
texto2 = 'Bom dia, estamos na aula de computational thinking'

for caractere in texto1:
    print(caractere)

espaco = 0
for caractere in texto2:
    if caractere ==  'a' or caractere == 'A':
        espaco +=1

print('O texto2 tem', espaco, 'espacos')

letraA = 0
for caractere in texto2:
    if caractere ==  'a' or caractere == 'A':
        letraA +=1

print('O texto2 tem', letraA, 'letras "A"')