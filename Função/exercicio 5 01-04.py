#exercicio 5

def conta_imc (peso, altura) :
    imc_conta = peso / (altura * altura)
    return imc_conta

def classificacao (imc) :
    if imc <= 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 <= 24.9:
        print("Peso normal")
    elif imc >= 25:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
   
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = conta_imc(peso, altura)
print("Seu imc é de", imc)
classificacao(imc)