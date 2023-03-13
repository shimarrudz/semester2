#Exemplo Menu

lista_cod = []
lista_nome = []
lista_senha = []

resp = "S"

while(resp != "N"):
    print("1 - Inserir usuário")
    print("2 - Exibir dados do usuário")
    opc = int(input("Digite a opção: "))
    if (opc == 1):
        try:
            cod = int(input("Digite o código do usuário"))
            nome = input("Digite o nome do usuário")
            senha = input("Digite a senha do usuário")
        except ValueError:
            print("Digite um valor númerico")
        else:
            lista_cod.append(cod)
            lista_nome.append(nome)
            lista_senha.append(senha)
        finally:
            print("Operação finalizada")

    elif (opc == 2):
            print(lista_cod)
            print(lista_nome)
            print(lista_senha)

    resp = input("Deseja continuar? S/N")

