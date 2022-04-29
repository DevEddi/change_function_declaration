'''
Esse código está sendo usado a refatoração
'''


def verificaFuncao(x):
    if x % 2 == 0:
        return 'Número par'
    else:
        return 'Número ímpar'

if __name__ == "__main__":

    while True:
        valor = int(input('Digite um valor:'))
        print(verificaFuncao(valor))
        y = input('Deseja continuar? (S|N): ')
        if y == 'N':
            break

        print('Digite apenas números')

