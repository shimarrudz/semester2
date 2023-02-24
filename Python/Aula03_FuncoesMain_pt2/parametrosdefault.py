## Criando um padrao, que quando nao for informado o periodo
## O parametro default reconhecera como tarde de qualquer jeito




#t = tarde
def saudacao (nome, periodo = "t"):
    if (periodo == "m"):
        print(f"Bom dia, {nome}!")
    elif (periodo == "t"):
        print(f"Boa tarde, {nome}!")
    elif (periodo == "n"):
        print(f"Boa noite, {nome}!")



