import json

with open('members.json') as arquivo:
    membros = json.load(arquivo)


nomes_membros = []
for membro in membros:
    nomes_membros.append(membro['ParliamentaryName'])

# fazer a linha 6, 7, 8 como copreensao de lista:
nomes_membros = [membro['ParliamentaryName'] for membro in membros]
print(nomes_membros)
