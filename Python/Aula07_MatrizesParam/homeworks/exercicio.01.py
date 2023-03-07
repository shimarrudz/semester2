#1) Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:

#· Uma função para carregar uma matriz 3x4 de números inteiros com a matriz sendo um parâmetro;

#· Uma função para exibir os elementos da matriz 3x4 com a matriz sendo um parâmetro;

#· Uma função que calcule e retorne a quantidade de números pares e ímpares contidos na matriz 3x4, a qual deve ser um parâmetro.


def carrega_matriz(matriz):
    for lin in range(0, 3):
        linha = []
        for col in range(0, 4):
            linha.append(int(input("Digite um elemento da matriz 3x4: ")))
        matriz.append(linha)


def exibe_matriz(matriz):
    for lin in range(0, 3):
        print(matriz[lin])


def quantidade_par_impar(matriz):
    impar = 0
    par = 0
    for lin in range(0, 3):
        for col in range(0, 4):
            if (matriz[lin][col] % 2 == 0):
                par += 1
            else:
                impar += 1

    return(par, impar)


def main():
    matriz = []
    carrega_matriz(matriz)
    exibe_matriz(matriz)
    print("Quantidade de pares e impares respectivamente: ", quantidade_par_impar(matriz))


if (__name__ == "__main__"):
    main()