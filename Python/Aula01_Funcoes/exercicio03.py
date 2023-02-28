# Uma função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá
# solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função
# valorPagamento. O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da
# prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(prestacao, diasAtraso):
    if (diasAtraso <= 0):
        return (prestacao)
    elif diasAtraso >= 1:
        pagamento = prestacao * 1.03
        return (pagamento)
    else:
        pagamento = prestacao * 1.03
        cont = 0
        while (cont < diasAtraso):
            pagamento = pagamento * 1.001
            cont = cont + 1
        return (pagamento)


valor_prestacao = float(input("Digite o valor da prestação: "))
quant_diasAtraso = int(input("Quantos foram os dias de atraso?:"))

print(
    f"O valor a ser pago é de: R${valorPagamento(valor_prestacao, quant_diasAtraso)}")


def valorPagamento(valor_prest, num_dias):
    if (num_dias < 1):
        novo_valor_prest = valor_prest
    else:
        valor_dias_atraso = valor_prest * (num_dias * (0.1/100))
        novo_valor_prest = (valor_prest * 1.03) + valor_dias_atraso
    return (novo_valor_prest)
