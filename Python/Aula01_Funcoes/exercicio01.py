#uma função que necessite de três parâmetros (números reais) e que retorne a soma desses três parâmetros.

def numeros_reais(num1, num2, num3):
    soma = num1 + num2 + num3
    return (soma)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

soma_tres_numeros = numeros_reais(num1, num2, num3)

print("A soma dos números reias é de: ", soma_tres_numeros)



