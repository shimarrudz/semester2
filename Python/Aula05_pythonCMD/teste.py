#Biblioteca que puxa os argumentos(parametros) do cmd para o código.
import sys

def main():
    if (len(sys.argv)==3):
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(soma_numeros(x,y))


def soma_numeros(x, y):
    soma = x + y
    return (soma)


if(__name__ == "__main__"):
    main()



