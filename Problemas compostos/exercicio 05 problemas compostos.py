# passo a passo

# 1 - exibir quantos litros de combustível e quantos reais é preciso pra fazer uma viagem de 800 km

# 2 - o carro tem 10 litros no tanque, ja percorreu 90 km, o combustível custa R$6,90, o carro tem autonomia de 7 km por litro

# 3
#1 descobrir quantos litros de combustivel é preciso pra viagem
#2 descobrir quantos reais é preciso pra fazer a viagem

print("viagem de carro")
quilometro= int(input("quantos km ainda falta percorrer "))
litros= int(input("digite quantos km por litro é gasto "))
n1= quilometro / litros

print("vai ser necessário = ", n1 , "litros")
preco= float(input("digite o preço da gasolina "))
n2= n1 * preco
print("o preço total é ", n2, "reais")