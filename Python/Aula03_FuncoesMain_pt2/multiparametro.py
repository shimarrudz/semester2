##Número desconhecido de parâmetros


def saudacao_pessoas(periodo, *nome):
    for n in nome:
        if (periodo == "m"):
            print(f"Bom dia, {n}!")
        elif (periodo == "t"):
            print(f"Boa tarde, {n}!")
        elif (periodo == "n"):
            print(f"Boa noite, {n}!")

saudacao_pessoas("t", "Maria", "Pedro", "Ana")






