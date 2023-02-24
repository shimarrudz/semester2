#Dada as listas abaixo, faça uma função que calcule o preço final de cada item dado os descontos para cada
# um deles. OBS: o programa deve ter, obrigatoriamente, a função “main”.


def main ():

    listaOriginal = [234, 64, 13467, 45.89, 23]
    listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

    listaDescontada = []
    for i in range(len(listaOriginal)):
        preco_original = listaOriginal[i]
        desconto = listaDescontos[i]
        preco_descontado = preco_original * (1 - desconto)
        listaDescontada.append(preco_descontado)


    print(listaDescontada)


if (__name__ == "__main__"):

    main()


