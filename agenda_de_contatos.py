'''desenvolver um a genda de contatos'''
'''primeiras funçõe 
1- consultar contatos -> feito
2- adicionar contatos -> FEITO
3- deletar contatos -> FEITO'''

dados=[]
registros = []

def menu_principal():
    print("--------------------------------------")
    print("|      ->AGENDA DE CONTATOS <-       |")
    print("--------------------------------------")
    print("|      [1] -> Mostrar contatos       |")
    print("|      [2] -> Adicionar contatos     |")
    print("|      [3] -> Deletar contato        |")
    print("--------------------------------------\n")
    resposta = int(input("Digite o numero correspondente a sua escolha: "))

    if resposta == 1:
        mostrar_contatos()
    elif resposta == 2:
        adiconar_contatos()
    elif resposta == 3:
        deletar_contatos()


def mostrar_contatos():
    for i in range(0, len(registros)):
        print("{} -- {}".format(registros[i][0], registros[i][1]))
    menu_principal()

def adiconar_contatos():
    quantidade = int(input("numero de contatos a adicionar: "))
    for i in range(0, quantidade):
        dados.append(str(input("nome do contato: ")))
        dados.append(str(input("numero do contato: ")))

        registros.append(dados[:])
        dados.clear()
    print("agenda de contatos atualizada ")
    menu_principal()

def deletar_contatos():
    nome = str(input("nome do contato para deletar: "))

    i = 0
    while i < len(registros):
        if nome in registros[i][0]:
            registros.pop(i)
            print("contato deletado")

        i = i + 1
    print("{} foi retirado da sua lsta de contatos".format(nome))
    menu_principal()

menu_principal()

