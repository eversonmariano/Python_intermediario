'''
1-crie uma funçao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
'''

# def olaMundo():
#     return 'Oi Mundo!'
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(olaMundo)
# print(executando)


'''
2-crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da 
funcao2 executada. Faça a funcao1 executar duas funçoes que recebam um numero
diferente de argumentos.
'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def falaOi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return  f'{saudacao} {nome}'

executando = mestre(falaOi, 'Ell')
executando2 = mestre(saudacao, 'Ell', saudacao='Bom dia!')
print(executando)
print(executando2)