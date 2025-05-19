import random

print("ADIVINHE O NÚMERO")
nome = str(input("Digite seu nome: "))
print("")
print("Olá", nome, "bem-vindo ao jogo!")

print("")
print("[0] Instrução")
print("[1] Jogar")
menu = int(input("Escolha uma opção: "))
print("")
n2 = random.randint(0, 100)
while True:
    
    if menu == 0:
        print("O jogo consiste na adivinhação, eu vou escolher um número de 0 a 100 e você terá que adivinhar qual número eu escolhi.")
        print("Durante o jogo vou falar se o número chutado é maior ou menor que o número escolhido.")
        print("Boa sorte!")
        print("")
        print("[1] Jogar")
        menu = int(input("Escolha uma opção: "))
        print("")
    
    elif menu == 1:
        n1 = int(input("Escolha um número de 0 a 100: "))
        
        if n1 < n2:
            print("O seu número é menor que o número escolhido")
                
        elif n1 > n2:
            print("O seu número é maior que o número escolhido")
                
        else:
            print("Parabéns, você acertou!")
            print("")
            print("[1] Continuar")
            print("[2] Sair")
            menu2 = int(input("Escolha uma opção: "))
            print("")
         
            if menu2 == 1:
                print("Vamos para outra rodada!")
                n2 = random.randint(0,100)
            else:
                print("Você saiu")
                break 
    
    
    
        