#MATRIZ 2 X 3
# 2 4 5
# 6 3 2

#Primeira sublista
matriz = [ [2, 4, 5,] , [6, 3, 2] ]

#Matriz completa como uma linha
print(matriz)

#Imprimir primeira linha da matriz
print(matriz[0])

#imprimir a segunda linha
print(matriz[1])

#Imprimir segundo elemento da primeira linha
print("Segundo elemento da primeira linha: ", matriz[0][1])

#Imprimir o segundo elemento da segunda linha
print("Segundo elemento da segunda linha: ", matriz[1][1])

#Imprimir a matriz no formato original
for lin in range(0, 2):
    print(matriz[lin])

#Exibir somente os elementos maiores do que 2 da matriz
for lin in range (0, 2):
    for col in range (0, 3):
        if (matriz [lin][col] > 2):
            print("Números maiores que 2: ", matriz[lin][col])
