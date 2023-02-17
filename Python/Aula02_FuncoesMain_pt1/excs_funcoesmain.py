def main():
    resp = "S"
    lista = []


    while (resp != "N"):
        print("1-Leitura dos 10 números")
        print("2-Encontrar número maior")
        print("3-Exibir lista")
        opc = int(input("Escolha uma opção: (1 a 3): "))

        if (opc == 1):
            leitura = carrega_lista(lista)

        if (opc == 2):
            maior = encontra_maior(lista)
            exibe_resultado(maior)

        if (opc == 3):
            exibe_resultado(lista)

        resp = input("Deseja continuar (S/N)?")

    carrega_lista(lista)
    exibe_resultado(lista)


def carrega_lista(lista):
    for i in range (0,10):
        num = int(input("Digite um número: "))
        lista.append(num)

    return (lista)


def encontra_maior(lista):
    maior = lista[0]
    for i in range (1,10):
        if (lista[i] > maior):
            maior = lista[i]

    return (maior)


def exibe_resultado(resultado):
    print(resultado)


if (__name__ == "__main__"):

    main()


