'''
Esse commit não está com alteração de função
'''

def verificaFuncao(x):
    if valor % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')

while True:
    try:
        valor = int(input('Digite um valor:'))
        verificaFuncao(valor)
        y = input('Deseja continuar? (S|N): ')
        if y == 'N':
            break
    except:
        print('Digite apenas números')