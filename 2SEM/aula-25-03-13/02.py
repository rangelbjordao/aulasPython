'''
Usa input para ler o float.
Enquanto a entrada nao for valida, imprime uma mensagem de erro e tenta novamente.
'''


def le_float():
    bem_sucedido = False
    while not bem_sucedido:
        try:
            entrada = float(input())
            bem_sucedido = True
        except:
            print('Valor invalido, Por favor digite um numero.')

    return entrada


print('Digite o primeiro numero:')
x = le_float()
print('Digite o segundo numero:')
y = le_float()

print(f'{x} + {y} = {x + y}')

try:
    print(f'{x} / {y} = {x / y}')
except ZeroDivisionError:
    print('Nao posso fazer x/y pois y=0')

print(f'{x} * {y} = {x * y}')
print(f'{x} - {y} = {x - y}')
