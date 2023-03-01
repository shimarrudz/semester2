#Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3)
# e mais 2 argumentos (números inteiros). O programa deverá ter uma função para checar e retornar qual é o menor número
# (opção 1), uma função para calcular a multiplicação desses números (opção 2) e outra para exibir todos os números dentro
# do intervalo definido pelos 2 argumentos numéricos (opção 3), desde que o primeiro número seja maior do que o segundo.
# OBS: o programa deve ter, obrigatoriamente, a função “main”.

import sys

def menor_numero(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

def multiplicacao(n1, n2):
    return n1 * n2

def exibir_intervalo(n1, n2):
    if n1 < n2:
        for i in range(n1, n2+1):
            print(i)
    else:
        print("O primeiro número deve ser maior que o segundo")

def main():
    if len(sys.argv) != 4:
        print("Uso: python programa.py <opcao> <numero1> <numero2>")
        return

    opcao = int(sys.argv[1])
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])

    if opcao == 1:
        print(menor_numero(n1, n2))
    elif opcao == 2:
        print(multiplicacao(n1, n2))
    elif opcao == 3:
        exibir_intervalo(n1, n2)
    else:
        print("Opção inválida")

if __name__ == '__main__':
    main()

