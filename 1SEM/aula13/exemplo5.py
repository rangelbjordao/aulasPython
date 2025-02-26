compras = ["alface", "banana", "iogurte"]
print(compras)

print()

compras[0] = "rucula"
compras[1] = "melancia"
print("Lista modificada:")
print(compras)

print()

compras.sort()
print("Lista modificada, agora em ordem crescente:")
print(compras)

print("\n---\n")

temperaturas = [19.1, 20.5, 21.3, 21.9, 23.0, 22.8, 19.0, 17.2]
menor_temp = min(temperaturas)
maior_temp = max(temperaturas)

print("Temperaturas:", temperaturas)
print("A maxima nesse dia foi", maior_temp)
print("A minima nesse dia foi", menor_temp)