#Lambda Com MAP
lista = [3, 5, 6, 2, 4, 10]

#Função sem map
calcula_dobro = lambda num : num * 2
print("Dobro: ", calcula_dobro(6))



#Lista dobro com map
lista_dobro = list(map(calcula_dobro, lista))



#O código mais compactado sem uso de funções
lista_dobro_nova = list(map(lambda num : num * 2, lista))





