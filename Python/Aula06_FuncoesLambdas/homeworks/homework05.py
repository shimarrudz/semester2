#Dada as listas abaixo, transforme a função que calcule o preço final de cada item dado os descontos para cada um deles
# em uma função lambda. Aperfeiçoe a aplicação escrevendo a função lambda diretamente dentro da chamada do MAP.
# listaOriginal = [234, 64, 13467, 45.89, 23]
# listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

listaOriginal = [234, 64, 13467, 45.89, 23]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

desconto_blackfriday = list(map(lambda preco, desc: preco * desc, listaOriginal, listaDescontos))

print(desconto_blackfriday)


