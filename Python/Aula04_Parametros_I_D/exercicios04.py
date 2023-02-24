#uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D
# de mesPorExtenso de AAAA.
# texto = ("Programar em phyton")  texto_split = texto.split("/")



def transformaData(data):
    dataQuebrada = data.split('/')
    dia = dataQuebrada[0]
    mes = dataQuebrada[1]
    ano = dataQuebrada[2]

    if mes == '01':
        mes = 'Janeiro'
    elif mes ==  '02':
        mes = 'Fevereiro'
    elif mes ==  '03':
        mes = 'Março'
    elif mes ==  '04':
        mes = 'Abril'
    elif mes ==  '05':
        mes = 'Maio'
    elif mes ==  '06':
        mes = 'Junho'
    elif mes ==  '07':
        mes = 'Julho'
    elif mes ==  '08':
        mes = 'Agosto'
    elif mes ==  '09':
        mes = 'Setembro'
    elif mes ==  '10':
        mes = 'Outubro'
    elif mes ==  '11':
        mes = 'Novembro'
    elif mes ==  '12':
        mes = 'Dezembro'

    result = dia + ' de ' + mes + ' de ' + ano
    return result

print(transformaData('08/09/2003'))


def mostra_data_extenso(data):
    lista_data = data.split("/")
    if(lista_data[1] == "01"):
        mes = "Janeiro"
    elif(lista_data[1] == "02"):
        mes = "Feveireiro"
    elif(lista_data[1] == "03"):
        mes = "Março"
    elif(lista_data[1] == "04"):
        mes = "Abril"
    elif(lista_data[1] == "05"):
        mes = "Maio"
    elif(lista_data[1] == "06"):
        mes = "Junho"
    elif(lista_data[1] == "07"):
        mes = "Julho"
    elif(lista_data[1] == "08"):
        mes = "Agosto"
    elif(lista_data[1] == "09"):
        mes = "Setembro"
    elif(lista_data[1] == "10"):
        mes = "Outubro"
    elif(lista_data[1] == "11"):
        mes = "Novembro"
    elif(lista_data[1] == "12"):
        mes = "Dezembro"

    data_por_extenso = lista_data[0] + " de " + mes + " de " + lista_data[2]
    return data_por_extenso


data = input("Qual a data que deseja receber o valor por extenso?")

resposta = print("A data por extenso será: ", mostra_data_extenso(data))
