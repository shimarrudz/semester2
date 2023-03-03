#Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3)
# e mais 1 argumento (tamanho da lista). O programa deverá ter uma função para carregar os elementos da lista original
# de acordo com o tamanho que deve ser passado como argumento (opção 1), uma função para criar e exibir outra lista com
# o triplo dos elementos da lista original (opção 2) e outra para exibir somente os elementos pares da lista original
# (opção 3), desde que o primeiro número seja maior do que o segundo. OBS: o programa deve ter,
# obrigatoriamente, a função “main”.

import sys

def carrega_lista(lista, tam):
    for i in range (0, tam):
        lista.append(int(input("Digite o elemento da lista: ")))


def calcula_triplo (lista,tam):
    lista_triplo = []
    for i in range (0,tam):
        lista_triplo.append(lista[i] * 3)

    return(lista_triplo)

def exibe_pares(lista,tam):
    for i in range (0,tam):
        if(lista[i] % 2 == 0):
            print(lista[i])

def main():
    if len(sys.argv) == 3:
        print("Uso: python programa.py <opcao> <tamanho_lista>")
        return

    opcao = int(sys.argv[1])
    tamanho = int(sys.argv[2])

    if (opcao == 1):
        lista = []
        carrega_lista(lista, tamanho)
    elif (opcao == 2):
        lista = []
        carrega_lista(lista, tamanho)
        print("Lista - trplo: ", calcula_triplo(lista,tamanho))
    elif opcao == 3:
        lista = []
        carrega_lista(lista, tamanho)
        exibe_pares(lista, tamanho)
    else:
        print("Opção inválida")

if __name__ == '__main__':
    main()