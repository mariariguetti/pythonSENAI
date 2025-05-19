#exercicio 2

def celsius_para_fahrenheit(temperatura):
    conta_fahrenheit = temperatura * 1.8 + 32
    return conta_fahrenheit

def celsius_para_kelvin(grau):
    conta_kelvin = grau + 273
    return conta_kelvin

def mostrar_conversao(temperatura):
    print("Agora está ", celsius_para_fahrenheit(temperatura), "fahrenheit")
    print("Agora está ", celsius_para_kelvin(temperatura), "kelvin")
    
temperatura = float(input("Qual a temperatura? "))

mostrar_conversao(temperatura)