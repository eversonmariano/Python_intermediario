
'''
FUNÇOES (DEF) EM PYTHON - *ARGS **KWARGS- AULA 16 (PARTE 3
'''

# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# # print(*lista, sep = '-')
# func(*lista, *lista2)

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, idade=37)