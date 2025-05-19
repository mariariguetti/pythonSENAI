import inputs

lista = []

while True:
    print("Menu")
    print("")
    print("[1] Cadastrar nomes")
    print("[2] Total de inscritos")
    print("[3] Lista de nomes em ordem alfabética")
    print("[4] Consulta de nome")

    menu = inputs.input_int("Digite uma opção: ")
    if menu == 1:
        nome = inputs.input_str("Digite seu nome completo: ")
        if nome in lista:
            print("Esse nome ja existe na lista")
        else:
            lista.append(nome)
            print("Seu nome foi adicionado")
            
    elif menu == 2:
        print(len(lista))
        
        
    elif menu == 3:
        for nome in lista:
            print(nome)
    elif menu == 4:
        if nome in lista:
            print("Nome encontrado!")
            print("[1] Sim")
            print("[2] Não")
            menu1 = inputs.input_int("Deseja removê-lo? ")
            if menu1 == 1:
                print("Seu nome foi removido")
            else:
                print("Continue a inscrição")
        else:
            print("Nome não encontrado")
            print("[1] Sim")
            print("[2] Não")
            menu2 = inputs.input_int("Deseja adicioná-lo? ")
            if menu2 == 1:
                nome.append("nome")
                print("Seu nome foi adicionado")
            else:
                break
            
            
            