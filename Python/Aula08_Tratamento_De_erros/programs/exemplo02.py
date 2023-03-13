#Evitar erros sérios que podem acontecer no banco de dados

#Divisão de dois números com tratamento de dados


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    divisao = num1 / num2

except ValueError:
    print("***** ERRO ***** \n Digite um valor númerico!")

except ZeroDivisionError:
    print("***** ERRO ***** \n Um número não pode ser divido por zero")
else:
    print(f"Divisão: {divisao:.2f}")

finally:
    print("Operação finalizada")

