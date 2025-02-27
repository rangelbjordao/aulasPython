valores = [3, 10, -6, 8, 47, 0, 5, 11, 9]


menores_que_10 = [valor for valor in valores if valor < 10]
print(menores_que_10)


# a linha 3 é equivalente a montar com append:
menores_que_10 = []
for valor in valores:
    if valor < 10:
        menores_que_10.append(valor)


'''
O metodo da linha 3 se chama "compreensao de lista" ou "list comprehension"
e é uma forma mais compacta de fazer essa tarefa que e bastante comum:
selecionar apenas os dados que passam em algum filtro.
'''

# Nao precisa ser um filtro simples, posso aplicar mais logica
dobro_dos_menos_que_10 = [2*valor for valor in valores if valor < 10]
print(dobro_dos_menos_que_10)
