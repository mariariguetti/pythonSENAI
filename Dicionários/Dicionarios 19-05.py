
objeto = {
    "Nome": "armário",
    "Altura": 1.80,
    "Cor": "marrom",
}
print(objeto)

objeto2 = {
    "Nome": "geladeira",
    "Altura": 1.90,
    "Cor": "branco",
}
print(objeto2)

objeto3 = {
    "Nome": "fogão",
    "Altura": 1.30,
    "Cor": "cinza",
}
print(objeto3)

# Exibir uma lista de Dicionários
lista_objeto = [objeto, objeto2, objeto3]

    # Escolhendo os campos
for objeto in lista_objeto:
    print(f"{objeto['Nome']}")

       # Exibindo todos
for objeto in lista_objeto:
    for chave, valor in objeto.items():
        print(f"{chave} - {valor}")
    print()
       
       
       
       
       
       
       