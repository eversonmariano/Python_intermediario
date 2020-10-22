'''
ZIP - UNINDO ITERÁVEIS
ZIP_LONGEST - ITERTOOLS
'''

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Campina Grande', 'Recife', 'Natal', 'Monte Belo']
estados = ['SP', 'PB', 'PE']

#estados_cidades = zip(estados, cidades)

# estados_cidades = zip_longest(
#     indice,
#     estados,
#     cidades,
#     fillvalue='Estado'
# )
estados_cidades = zip(
    indice,
    estados,
    cidades,

)

# for i in estados_cidades:
#     print(i)

#PARA DESEMPACOTAR OS VALORES:

for indice, estado, cidade in estados_cidades:
    print(indice, estado, cidade)


# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# for i in cidades_estados:
#     print(i)
#print(list(estados_cidades))
