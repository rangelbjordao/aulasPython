compras = []

print('Vamos criar a sua lista de compras!')
print('Quantos itens ela vai ter?')
n = int(input())

contador = 0
for i in range(n):
    contador += 1
    print('Digite o', contador, 'item:')
    compras.append(input())

print(compras)