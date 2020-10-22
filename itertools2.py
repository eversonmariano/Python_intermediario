'''
COMBINATIONS, PERMUTATIONS E PRODUCT - ITERTOOLS
COMBINAÇÃO - ORDEM NÃO IMPORTA
PERMUTAÇÃO - ORDEM IMPORTA
AMBOS NÃO REPETEM VALORES ÚNICOS
PRODUTO - ORDEM IMPORTA E REPETE VALORES ÚNICOS
'''
from itertools import combinations, permutations, product

pessoas = ['ell', 'beta', 'joao', 'pedro', 'jose', 'salvia']

for grupo in product(pessoas, repeat=2):
    print(grupo)
