#Faça funções lambdas que:
# Retorne o oposto de um número
oposto = lambda x: -x

oposto(7)

# Retorne o inverso de um número
inverso = lambda x: 1 / x

inverso(3)

# Calcule a metade de um número
metade = lambda x: x / 2

metade(5)

# Calcule a soma de quadrados de dois número
soma_quadrados = lambda num1, num2: num1 ** 2 + num2 ** 2


# Imprima o nome e idade de uma pessoa
nome_idade = lambda nome, idade: print("O nome e idade da pessoa respectivamente é :",nome, idade)

nome = "Victor"
idade = 19

nome_idade(nome, idade)


#Retorne 0 se o valor for PAR e 1 se for ÍMPAR
par_impar = lambda x : 0 if x % 2 == 0 else 1



# Calcule o triplo de um número
triplo_num = lambda x: x * 3



# Retorne se a pessoa é maior de idade
retorna_maiordeidade = lambda idade: print("Você é maior de idade ") if idade > 18 else print("Você é menor de idade")

idade = 19
retorna_maiordeidade(idade)

