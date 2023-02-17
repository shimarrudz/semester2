#Uma função chamada somaImposto, que possua dois parâmetros: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera”
# o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto, custo):
    taxaImposto = custo * taxaImposto / 100
    soma = taxaImposto + custo
    return(soma)


imposto_final = int(input("Digite a porcentagem do imposto: "))
custo_final = float(input("Digite o valor do custo: "))

soma_final = somaImposto(imposto_final, custo_final)

print("Custo final: ", soma_final)


def somaImposto(custo, taxa):
    novo_custo = custo + (custo *(taxa/100))
    return(novo_custo)

custo = 100
taxa = 20

print("\n")

print("Novo custo: ", somaImposto(custo,taxa))





