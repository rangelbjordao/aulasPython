mensagem = "  Esta mensagem contem varias coisas. Vamos usar como exemplo! "
print(mensagem)

mensagem = mensagem.strip()  # remove espacos sobrando no inicio e fim da string
print(mensagem)

print("Deseja continuar? (S/N)")
resposta = input()
resposta = resposta.lower()  # passa a resposta para letras minusculas
if resposta == "s":
    print("Ok, continuando!")
elif resposta == "n":
    print("Ok, parando...")
    exit()  # termina programa imediatamente
else:
    print("Nao entendi a resposta, nas vou continuar entao...")

print(mensagem.upper())
print(mensagem)

print("Fim")