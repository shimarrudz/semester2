#FUNÇÕES SEM RETORNO


##O nome da função não pode repertir o nome e nem ser igual a de um parametro ou variavel


#Exemplo 1
##Função def = Definindo uma função que aparece uma mensagem
##Função de mensagem não possui parametro

def exibe_mensagem():
    print("Primeira função em Python")

##Chamando a função, logo ela realiza o print
exibe_mensagem()


#Exemplo 2

##(mensagem)parametro formal= esta sendo criado na hora da definição da função
def exibe_mensagem_custom(mensagem):
    print(mensagem)


msg = "Mensagem do Prof. Daniel"
exibe_mensagem_custom(msg)

## msg = parametro real vai substituir o parametro formal
## passagem de parâmetros: parâmetro real substitui o parâmetro formal
## a passagem de parâmetros deve ser do mesmo type




#Exemplo 3

def soma_numeros (num1, num2):
    soma = num1 + num2
    print("Soma: ", soma)

x = 5
y = 13
soma_numeros(x, y)



#FUNÇÕES COM RETORNO

#Exemplo 1

def soma_numeros_retorno(num1, num2):
    soma = num1 + num2
    return (soma)

a = 7
b = 12

print("Soma: ", soma_numeros_retorno(a,b))




#Exemplo 2

def calcula_soma_media(a, b):
    soma = a + b
    media = (a + b) / 2
    return(soma, media)

v = 6
z = 12

calcula_soma_media(v,z)

s, m = calcula_soma_media(a, b)



#Exemplo 3
def par_impar(numero):
    if (numero % 2 == 0):
        return (1)
    else:
        return(0)


numero_novo = 9

resto = par_impar(numero_novo)

if(resto == 1):
    print("O número é par")
else:
    print("O número é ímpar")




#Exemplo 4  SEM RETORNO
def verifica_maior(x, y):
    if (x > y):
        print("Maior: ", x)
    else:
        print("Maior", y)


numx = 5
numy = 8

verifica_maior(numx, numy)




#Exemplo 5 COM RETORNO
def verifica_maior_retorno(x, y):
    if (x > y):
        return (x)
    else:
        return (y)

num1 = 5
num2 = 8

print("Maior", verifica_maior_retorno(num1,num2))

maior = verifica_maior_retorno(num1, num2)

dobro = maior * 2
print(dobro)



