
#Função sem o uso do MAP!
def calcula_desconto(lista_precos):
    lista_descontos = []
    for i in range (0,len(lista_precos)):
        lista_descontos.append(lista_precos[i] - (lista_precos[i] * 0.20))

    return (lista_descontos)

#Função com uso do MAP!

def calcula_desconto_map(preco):
    desconto = preco - preco * 0.20
    return (desconto)


def main():
    lista_precos = [300, 250.30, 150, 400.20, 730.10]
    print("***** Função sem o uso do MAP *****")
    lista_descontos = calcula_desconto(lista_precos)
    print(lista_descontos)
    print("\n***** Função com o uso do MAP *****")
    lista_descontos = list(map(calcula_desconto_map, lista_precos))
    print(lista_descontos)



if (__name__ == "__main__"):
    main()


