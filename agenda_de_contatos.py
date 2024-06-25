'''desenvolver um a genda de contatos'''
'''primeiras funçõe 
1- consultar contatos -> feito
2- adicionar contatos -> FEITO
3- deletar contatos -> FEITO'''

dados=[]
registros = []

def mostrar_contatos():
    for i in range(0, len(registros)):
        print("{} -- {}".format(registros[i][0],registros[i][1]))

def adiconar_dados():
    for i in range(0,4):
        dados.append(str(input("nome do contato: ")))
        dados.append(str(input("numero do contato: ")))

        registros.append(dados[:])
        dados.clear()

def deletar_dados():
    nome = str(input("nome do contato para deletar: "))

    i = 0
    parada = False
    while parada == False:
        while i < len(registros):
            for i in range(0, len(registros)):
                for p in range (0, 1):
                    if nome in registros[i][0]:
                        registros.pop(i)
                        print("contato deletado")
                        parada = True

            i = i + 1
    return registros


adiconar_dados()
mostrar_contatos()

deletar_dados()

print(registros)


