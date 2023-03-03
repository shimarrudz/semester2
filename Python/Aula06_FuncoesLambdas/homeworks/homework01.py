#Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3)
# e mais 2 argumentos (números inteiros). O programa deverá ter uma função para checar e retornar qual é o menor número
# (opção 1), uma função para calcular a multiplicação desses números (opção 2) e outra para exibir todos os números dentro
# do intervalo definido pelos 2 argumentos numéricos (opção 3), desde que o primeiro número seja maior do que o segundo.
# OBS: o programa deve ter, obrigatoriamente, a função “main”.

import sys

def retorna_menor (x, y):
    if (x < y):
        return (x)
    else:
        return (y)

def calcula_mult (x, y):
    mult = x * y
    return(mult)


def exibe_numeros (x, y):
    #y: início e x: fim
    if (x > y):
        cont = y
        while (cont <= x):
            print(cont)
            cont = cont + 1
    else:
        print("Não é possível exibir os números.")

def main():
    if(len(sys.argv)==4):
        opc = int(sys.argv[1])
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        if (opc == 1):
            print("Menor número: ", retorna_menor(x, y))
        elif (opc == 2):
            print("Multiplicação: ", calcula_mult(x, y))
        elif(opc == 3):
            exibe_numeros(x,y)
        else:
            print("Opção inválida")



if __name__ == '__main__':
    main()

