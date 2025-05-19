# passo a passo

# 1 - exibir quanto custa encher um tanque de 50 litros de um carro

# 2 - o tanque tem 50 litros de capacidade, está com 20 litros atualmente, o custo do combustivel é de R$5,80/litro

# 3
#1 descobrir quantos litros faltam para encher o tanque
#2 fazer a subtração 50 - 20
#3 descobrir quanto custa 30 litros de combustível
#4 fazer a multiplicação 30 * 5,80
#5 exibir o custo do combustível

capacidade_total= int(input("digite a capacidade do tanque "))
combustivel= int(input("digite quantos litros de combustível tem no tanque "))
resultado= capacidade_total - combustivel

preco= float(input("digite quanto custa o litro do combustível "))
resultado2= resultado * preco

print(" o custo foi de R$", resultado2)
