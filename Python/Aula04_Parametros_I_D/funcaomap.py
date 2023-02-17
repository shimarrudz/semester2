#Calcular uma funcao que mapeia a lista multiplicando-a por 2
#Map funciona com variaveis iteraveis(que possuem indice)

def calculadora_dobro(x):
    dobro = x * 2
    return(dobro)

lista = [1, 2, 3, 4, 5, 6,]
lista_dobro = list(map(calculadora_dobro,lista))

print(lista_dobro)



