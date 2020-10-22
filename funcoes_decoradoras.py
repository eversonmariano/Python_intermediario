'''Envolve as funçoes que vc quiser,
    mudando ou não o comportamento delas,
    caso vc prefira.'''

# def fala_oi():
#     print('Oi!')
#
# variavel = fala_oi()

# '''funçao decoradora'''
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return slave

# def fala_oi():
#     print('OI!!!')

# variavel = master(fala_oi)
# variavel()

'''FUNÇAO DECORADORA'''
# fala_oi = master(fala_oi)
# fala_oi()

# '''decorador'''
# @master
# def fala_oi():
#     print('OI!!!')
#
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
# outra_funcao('Eu sou o japa!')

from time import time
from time import sleep

def velocidade(funcao):
    def slave(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f} milisegs p/ executar.')
    return slave

@velocidade
def demora():
    for i in range(100000000000000):
        print(i, end='\n')


demora()








