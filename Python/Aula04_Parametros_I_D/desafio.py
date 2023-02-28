#Utilizando o conceito do número desconhecido de parâmetros de uma função crie uma função que faça a conversão e extenso
#de uma data no formato "DD/MM/AAAA". OBS: não deve ser utilizado if, elif ,ele no corpo da função

def extenso_data(data, *meses):
    lista_data = data.split("/")
    data_extenso = lista_data[0] + " de " + meses[int(lista_data[1])-1]



receberData = input("Digite a data no formato DD/MM/AAAA:  ")
extenso_data(receberData, "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")


print(extenso_data(receberData))
