#Função 1
def exibe_mensagem():
    print("Olá")


#Função 2
def soma_numeros(x,y):
    soma = x + y
    return(soma)

#Função Main
def main():

    exibe_mensagem()
    x = 7
    y = 9
    print("Soma: ", soma_numeros(x,y))

#Checagem da main. "__name__" é uma variável padrão do python
if(__name__ == "__main__"):

    main()



