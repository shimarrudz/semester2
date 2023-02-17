#Criando dicionários com parametros indefinidos

def saudacao (periodo, **nome):
    if (periodo == "m"):
        print(f"Bom dia, {nome['sobrenome']}!")
    elif (periodo == "t"):
        print(f"Boa tarde, {nome['sobrenome']}!")
    else:
        print(f"Boa noite, {nome['sobrenome']}!")



saudacao("t", nome = "João", sobrenome = "Souza")
