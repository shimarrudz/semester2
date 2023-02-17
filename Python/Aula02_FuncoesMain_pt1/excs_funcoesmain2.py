def main():
    resp = "S"
    x = 0
    y = 0

    while (resp != "N"):
        print("1-Leitura")
        print("2-Soma")
        print("3-Subtração")
        print("4-Multiplicação")
        print("5-Divisão")
        opc = int(input("Escolha a opção (1 a 5): "))
        if (opc == 1):
            x,y = leitura()  #serao atribuidos valores nas variasveis x,y respectivamente
        elif (opc == 2):
            soma = soma_numeros(x,y)
            exibe_resultado(soma)
        elif (opc == 3):
            sub = sub_numeros(x,y)
            exibe_resultado(sub)
        elif (opc == 4):
            mult = mult_numeros(x,y)
            exibe_resultado(mult)
        elif (opc == 5):
            div = div_numeros(x,y)
            exibe_resultado(div)
        else:
            print("Opção Inválida")

        resp = input("Deseja continuar (S/N)? ")




#Não necessita parâmetros pois o valor será lido dentro da função
def leitura():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    return (x,y)

def soma_numeros(x,y):
    soma = x + y
    return(soma)


def sub_numeros(x,y):
    sub = x - y
    return(sub)

def mult_numeros(x,y):
    mult = x * y
    return(mult)

def div_numeros(x,y):
    div = x / y
    return(div)


def exibe_resultado(resultado):
    print(f"Resultado:{resultado:.2f}")

if (__name__ == "__main__"):

    main()
