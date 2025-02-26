compras = ["alface", "banana", "iogurte"]
print(compras)

print()

# (1) modificar elementos
compras[0] = "rucula" #coloco rucula no lugar de alface
compras[1] = "melancia" #coloco melancia no lugar de banana
print("Lista modificada:")
print(compras)

# (2) adicionar elementos
compras.append("escova de dente")
print(compras)

print()

# tamber existe o extend e o insert

# (3) remover elementos
compras.remove("iogurte") # busca o valor na lista, se encontrar, remove
print("Apos remover iogurte:")
print(compras)