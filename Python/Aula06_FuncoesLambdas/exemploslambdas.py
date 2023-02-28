
#Função de soma
def soma_numeros(a, b):
    soma = a = b
    return(soma)

a = 8
b = 9

print("Soma: ", soma_numeros(a, b))

#Função soma lambda
soma_numeros_lambda = lambda a, b : a if a > b else b

a2 = 7
b2 = 6

print("Soma: ", soma_numeros_lambda(a,b))




#Função comum de número maior
def retorna_maior (a, b):
    if (a > b):
        return
    else:
        return (b)

x = 4
y = 9

print("Maior normal: ", retorna_maior(x, y))

#Função lambda número maior

retorna_maior_lambda = lambda a, b : a if a > b else b


x2 = 12
y2 = 7

print("O maior é: ", retorna_maior_lambda(a, b))

