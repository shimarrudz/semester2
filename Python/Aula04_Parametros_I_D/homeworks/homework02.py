#Faça uma função comum que calcule 20% de desconto para a próxima black Friday. Utilize-a numa lista que tem
# os preços dos itens que você planeja comprar. Faça isso primeiro sem MAP e depois com MAP. OBS: o programa
# deve ter, obrigatoriamente, a função “main”.


def calc_desconto(preco):
    return preco * 0.8

def desconto_black(x):
    desconto = x * 0.80
    return(desconto)


def main():


    lista = [100.50, 48.8, 37, 89, 60, 120,]
    lista_desconto = list(map(desconto_black,lista))

    print(f" \n O valor do desconto com map:  {lista_desconto}\n \n")



    precos = [100, 50, 80, 120]
    precos_descontados = []
    for preco in precos:
        preco_descontado = calc_desconto(preco)
        precos_descontados.append(preco_descontado)
    print(f"O valor do desconto sem map: {precos_descontados} ")


if (__name__ == "__main__"):

    main()



