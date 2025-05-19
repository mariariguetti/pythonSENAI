#passo 1: criar uma lista com os nomes de 5 objetos

objetos = ["Lápis", "Borracha", "Cola", "Tesoura", "Apontador"]

#passo 2: adicionar mais um objeto ao final da lista

objetos.append("Caneta")

#passo 3: acessar o objeto que está na 2 posição e exiba-o

print(objetos[1])

#passo 4: remover um objeto da lista e exibir

print(objetos.pop(2))

#passo 5: exiba o tamanho da lista

print(len(objetos))

#passo 6: mostrar todos os itens com o for

for objeto in objetos:
    print(objeto)

#passo 7: verificar se "cadeira" está na lista. Se sim remova-a, se não adicione
    
if "cadeira" in objetos:
    objetos.remove("Cadeira")
    print("Cadeira removida")
else:
    objetos.append("Cadeira")
    print("Cadeira adicionada")
    
#passo 8: ordenar a lista em ordem alfabética, exiba o antes e o depois

print(objetos.sort())
print(objetos)

#passo 9: exiba o primeiro e o último objeto e exiba eles

print(objetos[0])
print(objetos[len(objetos)- 1])

#passo 10: limpar toda a lista

objetos.clear()
    
    
    
    
    
    