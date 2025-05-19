print("")

def input_str(mensagem):
    while True:
        nome = str(input(mensagem))
        
        if not nome.isalpha():
            print("Digite apenas letras")
        else:
            return nome

def input_int(mensagem):
    while True:
        try:    
            numero_int= int(input(mensagem))
            return numero_int    
        except ValueError:
            print("Digite apenas letras")
        
def input_float(mensagem):
    while True:
        try:
            numero_float = float(input(mensagem))
            print("Digite apenas letras")
        except ValueError:
            return nome 