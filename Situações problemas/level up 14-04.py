import random

print("PAR OU ÍMPAR")
print("Olá jogador, bem-vindo ao jogo!")
print("Escolha uma das opções Par ou Ímpar e vamos jogar!")


while True:
    print("[1] SAIR")
    print("[2] PAR")
    print("[3] ÍMPAR")
    menu = int(input("Escolha: "))
    n1 = int(input("Digite um número de 0 a 10: "))
    n2 = random.randint(1, 10)
    soma = n1 + n2
    print("")
    print("O jogo escolheu o número: ", n2)
    print("Você escolheu o número: ", n1)
    print("")
    if menu == 1:
        print("Você saiu")
        break
    elif menu == 2 and soma % 2 == 0:
        print("O resultado é ", soma, ", número par, você ganhou!")
    elif menu == 2 and soma % 2 == 1:
        print("O resultado é ", soma, ", número ímpar, você perdeu")
    elif menu == 3 and soma % 2 == 0:
        print("O resultado é ", soma, ", número par, você perdeu")
    else:
        print("O resultado é ", soma, ", número ímpar, você ganhou!")
        
    