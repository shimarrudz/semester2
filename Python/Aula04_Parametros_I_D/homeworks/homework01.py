#Utilizando o conceito do número indeterminado de argumentos chave, crie uma função que imprima o nome,
# sobrenome e idade de uma pessoa desde que ela tenha mais de 20 anos. #dica use chaves pnome, psobrenome,
# pidade. OBS: o programa deve ter, obrigatoriamente, a função “main”.


def exibe_pessoa(**pessoa):
        if (pessoa['pidade'] > 20):
            print(f"Nome: {pessoa['pnome']}, Sobrenome: {pessoa['psobrenome']}, Idade: {pessoa['pidade']}")

def main():
    exibe_pessoa(pnome='João', psobrenome='Silva', pidade=30)
    exibe_pessoa(pnome='Maria', psobrenome='Souza', pidade=18)
    exibe_pessoa(pnome='Pedro', psobrenome='Lima', pidade=56)
    exibe_pessoa(pnome='Ana', psobrenome='Costa', pidade=25)

if __name__ == '__main__':
    main()



