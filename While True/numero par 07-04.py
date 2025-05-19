n = int(input("Digite um número par "))
quant = 0

while True:
    n = n - 1
    if n % 2 == 0:
        print(n)
        quant = quant + 1
    elif n <= 0:
        print("A quantidade é", quant + 1)
        break 