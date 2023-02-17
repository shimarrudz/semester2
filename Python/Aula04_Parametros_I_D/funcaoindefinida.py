# "*" Está definindo um parâmetro multivalorado
def saudacao (periodo, *nomes):
    for n in nomes:
        if (periodo == "m"):
            print(f"Bom dia, {n}!")
        elif (periodo == "t"):
            print(f"Boa tarde {n}!")
        else:
            print(f"Boa noite{n}!")


saudacao("m", "Gabriel", "Maria", "Pedro", "João")


