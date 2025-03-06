temperaturas = []
with open('dados.txt') as arquivo:
    for linha in arquivo:
        temperaturas.append(float(linha))

print('Eu montei a lista de temperaturas com tamanho', len(temperaturas))
'''
Exercício: crie (usando compreensão de lista):
    (a) temperaturas_altas, contendo as temperaturas acima de 90

    (b) temperaturas_muito_altas, contendo as temperaturas acima de 100

Depois vamos ver o tamanho dessas listas comparadas com a lista total
de temperaturas, para ver qual proporção do tempo está em temperatura alta
'''

'''
# construcao tradicional, sem compreensao de lista
temperaturas_altas = []
for temp in temperaturas:
    if temp > 90:
        temperaturas_altas.append(temp)
'''

# construcao equivalente com compreensao de lista
temperaturas_altas = [temp for temp in temperaturas if temp > 90]

print(f'Destas, {len(temperaturas_altas)} sao altas (acima de 90C).')

proporcao_altas = (len(temperaturas_altas)/len(temperaturas))
# porcentagem = '{:.0%}'.format(proporcao_altas)
print(
    f'Portanto a proporcao de temperaturas altas e de {100*proporcao_altas}%')

temperaturas_muito_altas = []
for temp in temperaturas:
    if temp > 100:
        temperaturas_muito_altas.append(temp)
