# sequencia de dados tambem permite testar existencia de elementos na sequencia

compras = ["alface", "banana", "iogurte"]
if "banana" in compras:
    print("preciso comprar banana")
    
if "manga" not in compras:
    print("nao preciso comprar manga")
    
mensagem = "estamos chegando ao final da aula..."
if "a" in mensagem:
    print("A mensagem contem a letra a")
    
if "oi" in mensagem:
    print("A mensagem contem oi")
else:
    print("A mensagem nao contem oi")
    
if "final" in mensagem:
    print("a mensagem contem a palavra final")