'''
count - é uma função que retornará um iterador
'''
from itertools import count

#contador = count(start=1, step=10)
#contador = count(start=2, step=2.25)
# contador = count(start=9, step=-1)
#
# for i in contador:
#     print(round(i, 2))
#
#     if i >= 10 or i <= -10:
#         break

contador = count()
lista = ['ell', 'pedro', 'paulo', 'beta']
lista = zip(contador, lista)
print(list(lista))