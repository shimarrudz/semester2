#1) Escreva um programa em Python que faça a inserção e exibição em 4 listas, as quais devem conter os seguintes dados:

#a. Código
#b. Nome do funcionário
#c. Idade do funcionário
#d. Salário do funcionário

#Faça o tratamento de erros no processo de inserção das listas. As operações (inserção e exibição) deverão
# ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).

lista_codigo = []
lista_nome_funcionario = []
lista_idade_funcionario = []
lista_salario_funcionario = []

resp = "S"

while(resp != "N"):
    print("1 - Inserir dados funcionário ")
    print("2 - Exibir dados do funcionário")
    opc = int(input("Digite a opção: "))
    if (opc == 1):
        try:
            codigo = int(input("Digite o código do usuário: "))
            nome = input("Digite o nome do funcionário: ")
            idade = int(input("Digite a idade do usuário: "))
            salario = float(input("Digite o salário do funcionário: "))

        except ValueError:
            print("Digite o tipo de dado correto!")
        else:
            lista_codigo.append(codigo)
            lista_nome_funcionario.append(nome)
            lista_idade_funcionario.append(idade)
            lista_salario_funcionario.append(salario)
        finally:
            print("Operação finalizada")

    elif (opc == 2):
            print("O código do funcionário é: ", lista_codigo)
            print("O nome do funcionário é ", lista_nome_funcionario)
            print("A idade do funcionário é: ",  lista_idade_funcionario)
            print(f"O salario do funcionário é {lista_salario_funcionario: .2f}")

    resp = input("Deseja continuar? S/N")

