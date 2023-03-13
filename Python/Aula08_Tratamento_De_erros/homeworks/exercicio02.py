#2) Escreva um programa em Python que faça a inserção e exibição em 4 listas, as quais devem conter os seguintes dados:

#a. Código
#b. Descrição do produto
#c. Quantidade em estoque
#d. Valor do produto

#Faça o tratamento de erros no processo de inserção das listas. As operações (inserção e exibição) deverão ser
# executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).

lista_codigo = []
lista_desc_produto = []
lista_quant_estoq = []
lista_preco = []

resp = "1"

while (resp != "0"):
    print("A - Inserir dados do produto ")
    print("B - Exibir dados do produto ")
    opc = input("Digite sua opção: ")

    if(opc == "A"):
        try :
            codigo = int(input("Digite o código do produto: "))
            descricao = input("Digite a descrição do produto: ")
            quant_estoque = int(input("Digite a quantidade de estoque: "))
            preco = float(input("Digite o preço do produto: "))

        except ValueError:
            print("***** ERRO ***** Este tipo de dado não é valido no campo preenchido")
        else:
            lista_codigo.append(codigo)
            lista_desc_produto.append(descricao)
            lista_quant_estoq.append(quant_estoque)
            lista_preco.append(preco)

    elif (opc == "B"):
        try:
            print("O código do produto: ", lista_codigo)
            print("Descrição do produto: ", lista_desc_produto)
            print("Quantidade de estoque do produto: ", lista_quant_estoq)
            print("Preço do produto: ", lista_preco)
        except ValueError:
            print("***** ERRO ***** Este tipo de dado não é valido no campo preenchido")

    resp = input("Você deseja continuar?  (A-SIM) - (B-NÃO)")

