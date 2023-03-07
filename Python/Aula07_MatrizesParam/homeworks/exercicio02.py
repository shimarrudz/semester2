#2) Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:

#· Uma função para carregar uma matriz 3x3 de números inteiros com a matriz sendo um parâmetro;

#· Uma função para exibir os elementos da matriz 3x3 com a matriz sendo um parâmetro;

#· Uma função que calcule e retorne a soma dos elementos da diagonal principal da matriz 3x3, a qual deve ser um parâmetro


def carrega_lista(matriz):
    for lin in range (0, 3):
        linha = []
        for col in range(0, 3):
            linha.append(int(input("Digite o elemento da matriz 3x3: ")))
        matriz.append(linha)

def exibe_matriz(matriz):
    for lin in range(0, 3):
        print(matriz[lin])

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(0, 3):
        soma += matriz[i][i]
    return soma



def main():
    matriz = []
    carrega_lista(matriz)
    exibe_matriz(matriz)
    print("A soma da diagonal principal da matriz é: ", soma_diagonal_principal(matriz))



if (__name__ == "__main__"):
    main()



