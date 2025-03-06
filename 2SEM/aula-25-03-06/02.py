import json

with open('members.json') as arquivo:
    membros = json.load(arquivo)


nomes_membros = [membro['ParliamentaryName'] for membro in membros]

# nomes_membros.sort()
# for nome in nomes_membros:
#     print(nome)


# Exercicio: criar lista com nomes de membros cujo atributo "IsCurrent" seja False
nomes_membros_inativos = []
nomes_membros_ativos = []
for membro in membros:
    nome = membro['ParliamentaryName']
    if membro['IsCurrent'] is True:
        nomes_membros_ativos.append(nome)
    else:
        nomes_membros_inativos.append(nome)
        
print('')
print('Nomes de membros atuais (em exercicio):')
nomes_membros_ativos.sort()
for nome in nomes_membros_ativos:
    print(nome)
# membros_inativos = [membro['ParliamentaryName'] for membro in membros if membro['IsCurrent'] == False]
