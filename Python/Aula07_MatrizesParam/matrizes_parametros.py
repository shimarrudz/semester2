#Essa função carrega qualquer tamanho de matrizes
def carrega_matriz(matriz, numLinha, numCol):
    for lin in range (0, numLinha):
        linha = []
        for col in range (0, numCol):
            linha.append(int(input("Digite o elemento:" )))
        matriz.append(linha)


def exibe_matriz(matriz, numLin):
    for lin in range (0, numLin):
        print(matriz[lin])


def soma_matriz(matriz, numLin, numCol):
    soma = 0
    for lin in range(0, numLin):
            for col in range(0, numCol):
                soma += matriz[lin][col]

    return(soma)


def main():
    matriz = []
    carrega_matriz(matriz,  3, 4)
    exibe_matriz(matriz, 3)
    print("Soma dos elementos da matriz: ", soma_matriz(matriz, 3, 4))



if (__name__ == "__main__"):
    main()