#Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3)
# e mais 1 argumento (tamanho da lista). O programa deverá ter uma função para carregar os elementos da lista original
# de acordo com o tamanho que deve ser passado como argumento (opção 1), uma função para criar e exibir outra lista com
# o triplo dos elementos da lista original (opção 2) e outra para exibir somente os elementos pares da lista original
# (opção 3), desde que o primeiro número seja maior do que o segundo. OBS: o programa deve ter,
# obrigatoriamente, a função “main”.

import sys
import random

def carregar_lista(tamanho):
    lista = [random.randint(1, 100) for _ in range(tamanho)]
    return lista

def triplo_elementos(lista):
    nova_lista = [elemento * 3 for elemento in lista]
    return nova_lista

def elementos_pares(lista):
    nova_lista = [elemento for elemento in lista if elemento % 2 == 0]
    return nova_lista

def main():
    if len(sys.argv) != 3:
        print("Uso: python programa.py <opcao> <tamanho_lista>")
        return

    opcao = int(sys.argv[1])
    tamanho = int(sys.argv[2])

    lista = carregar_lista(tamanho)

    if opcao == 1:
        print(lista)
    elif opcao == 2:
        nova_lista = triplo_elementos(lista)
        print(nova_lista)
    elif opcao == 3:
        nova_lista = elementos_pares(lista)
        print(nova_lista)
    else:
        print("Opção inválida")

if __name__ == '__main__':
    main()