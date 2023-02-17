#Uma função que carregue uma lista com 10 elementos e, em seguida, outra função que retorne
# o maior elemento dessa lista.

def carrega_lista(lista):
    for i in range (0,10):
        num = int(input("Digite um número: "))
        lista.append(num)

    return (lista)

lista = []
carrega_lista(lista)



def encontra_maior(lista):
    maior = lista[0]
    for i in range (1,10):
        if (lista[i] > maior):
            maior = lista[i]

    return (maior)


