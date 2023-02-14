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

print(soma_final)

