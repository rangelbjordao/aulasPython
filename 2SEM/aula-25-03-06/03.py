import json

with open('cambio_usd.json') as arquivo:
    dicionario_cambio = json.load(arquivo)

# o campo rates traz todas as taxas de cambio de quanto vale 1 USD em outras moedas

taxas = dicionario_cambio['rates']

# print(taxas)

'''
Exercicio: contruir umas lista das moedas que valem mais do que o USD.
Ou seja, aquelas moedas tais que 1 USD vale menos do 1 dessa moeda.
'''

moedas_especiais = []
# vamos percorrer todas as chaves do dicionario, que sao diferentes moedas
for moeda in taxas:
    if taxas[moeda] < 1:
        moedas_especiais.append(moeda)

print('Lista de moedas que valem mais do que o dolar')
for moeda in moedas_especiais:
    print(moeda)
