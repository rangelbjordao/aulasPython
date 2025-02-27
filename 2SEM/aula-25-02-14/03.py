import json

with open('members.json') as arquivo:
    membros = json.load(arquivo)

nomes_membros = []
for membro in membros:
    nomes_membros.append(membro['ParliamentaryName'])

lista_ordenada = sorted(nomes_membros)

for nome in lista_ordenada:
    print(nome)