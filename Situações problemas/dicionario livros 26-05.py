def cadastro (isbn, titulo, autor, categoria, ano_da_publicacao):
    livro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano da publicacao": ano_da_publicacao,
}
    livros.append(livro)
    
livros = []


while True:
    print("Menu das funções")
    print("")

    print("[1] Cadastro")
    print("[2] Exibir livros cadastrados ")
    print("[3] Quantidade total de livros cadastrados")
    print("[4] Lista de títulos")
    print("[0] Sair")
    print("")
    
    menu = int(input("Escolha uma opção:  "))
    if menu == 0:
        print("Você saiu!")
        break
        
    elif menu == 1:
        isbn = int(input("Digite o ISBN do livro: "))
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        categoria = input("Digite a categoria do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação do livro: "))

        cadastro(isbn, titulo, autor, categoria, ano_publicacao)
        print("Você cadastrou o seu livro")
            
    elif menu == 2:
        for livro in livros:
            for chave, valor in livro.items():
                print(f"{chave} - {valor}")
               
    elif menu == 3:
        print(len(livros))
            
    elif menu == 4:
        for livro in livros:
            print(livros[1])
        
