'''
O programa a seguir levanta dados do usuario e os armazena em um arquivo de configuraçao chamado config.txt

ATENCAO: em um cenario real, nao gravar dados sensiveis na forma de texto puro.
(CPF, cartao de credito, data de nascimentos, dados medicos...
tudo isso precisa ser criptografado)
'''

print('Qual o seu nome?')
nome = input()
print('Qual sua idade?')
idade = int(input())
print('Qual sua altura?')
altura = float(input())

# cria um arquivo de configuração para salvar os dados recebidos
arquivo_config = open('config.txt', 'w')

arquivo_config.write(nome + '\n')
arquivo_config.write(str(idade) + '\n')
arquivo_config.write(str(altura) + '\n')

arquivo_config.close()