

print("MENU")
print("")
print("[1] Cadastro completo")
print("[2] Exibir lista de cadastros")

    
menu = int(input("Escolha uma opção: "))

def cadastrar_aluno(alunos):
    aluno = {
        "Nome": nome,   
        }
    print("Cadastro feito")
    m = calcular_media(n1, n2, n3)
    s = verificar_situacao(m)
    aluno["media"] = m
    aluno["situacao"] = s
    alunos.append(aluno)
def calcular_media(n1, n2, n3):
        media = (n1 + n2 + n3) / 3 
        return media
    

def verificar_situacao(media):
    if calcular_media(n1, n2, n3) >= 7:
        return "Aprovado"
    
    elif calcular_media(n1, n2, n3) >= 5 and media <= 6.9:
        return "Recuperação"
        
    elif calcular_media(n1, n2, n3) <= 4:
        return "Reprovado"

    
def mostrar_relatorio(alunos):
    for aluno in alunos:
        for chave, valor in aluno.items():
            print(f"{chave} - {valor}")
# ------ lista
alunos = []      


# -----  codigo
while True:
    print("MENU")
    print("")
    print("[1] Cadastro completo")
    print("[2] Exibir lista de cadastros")
   
    
    menu = int(input("Escolha uma opção: "))
    
    if menu == 1:
        nome = str(input("Digite o nome completo: "))
        n1 = float(input("Digite sua primeira nota: "))
        n2 = float(input("Digite sua segunda nota: "))
        n3 = float(input("Digite sua terceira nota: "))
        cadastrar_aluno(alunos)
    
        calcular_media(n1, n2, n3)    
        verificar_situacao(calcular_media(n1, n2, n3))
    
    elif menu == 2:
        mostrar_relatorio(alunos)
            










