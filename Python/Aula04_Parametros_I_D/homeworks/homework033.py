#Função sem usar o MAP!
def calcula_desconto(lista_precos, lista_descontos):
    lista_precos_descontos = []
    for i in range (0, len(lista_precos)):
        lista_precos_descontos.append(lista_precos[i] - lista_precos[i] * lista_descontos[i])

    return(lista_precos_descontos)


def calcula_desconto_map(preco, desconto):
    preco_desconto = preco - (preco * desconto)
    return(preco_desconto)



def main():
    lista_precos = [300, 250.50, 150, 400.20, 730.10]
    lista_descontos = [0.30, 0.4, 0.08, 0.10, 0.20]
    print("\n***** Função com o uso do MAP *****")
    lista_preco_descontos = calcula_desconto(lista_precos, lista_descontos)
    print(lista_preco_descontos)
    print("\n***** Função com o uso do MAP *****")
    lista_preco_descontos = list(map(calcula_desconto_map, lista_precos, lista_descontos))
    print(lista_preco_descontos)



if (__name__ == "__main__"):

    main()