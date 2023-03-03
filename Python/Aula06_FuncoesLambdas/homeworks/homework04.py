#Transforme a função de descontos da Black Friday (20% de desconto ) em uma função lambda e aplique a sua coleção.
# Aperfeiçoe a aplicação escrevendo a função lambda diretamente dentro da chamada do MAP.

lista = [180, 150.50]
desconto_blackfriday = list(map(lambda desc: desc * 0.80, lista))

print(desconto_blackfriday)

