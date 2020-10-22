from dados import produtos, pessoas, lista
from functools import reduce

###############################################################################
# FUNÇÃO MAP().
##################################################################################

# nova_lista = map(lambda x: x * 2, lista)
# print(lista)
# print(list(nova_lista))

# def aumentaPreco(p):
#     p['preço'] = round(p['preço'] * 1.05, 2)
#     return p
#
#
#
# #precos = map(lambda p: p['preço'], produtos)
# novos_precos = map(aumentaPreco, produtos)
#
#
# for i in novos_precos:
#     print(i)

#nomes = map(lambda p: p['nome'], pessoas)

# def aumentaIdade(p):
#     p['idade'] = p['idade'] + 10
#     return p
#
#
# idades = map(aumentaIdade, pessoas)
#
# for pessoa in idades:
#     print(pessoa)


##################################################################################
# FUNÇÃO FILTER()
###################################################################################

#nova_lista = [x for x in lista if x > 5] compreensao de lista

# def filtra(produto):
#     if produto['preço'] > 50:
#         return True

# def filtra(pessoa: bool) -> bool:
#     if pessoa['idade'] < 18:
#         return True
#
# #nova_lista = filter(lambda p: p['preço'] < 10, produtos)
# nova_lista = filter(filtra, pessoas)
#
# # for produto in nova_lista:
# #     print(produto)
#
# for pessoa in nova_lista:
#     print(pessoa)

#print(list(nova_lista))

###########################################################################
############# FUNÇÃO REDUCE() ##################################################
#################################################################################
# A FUNÇÃO REDUCE É UM ACUMULADOR COMPULSIVO.

# acumula = 0
# for item in lista:
#     acumula += item
#
# print(acumula)

# valor_inicial = 0
# soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, valor_inicial)
#
# print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(f'A soma dos preços é {soma_precos}')
media = soma_precos/len(produtos)
print(f'A media de preço é {media}')

soma_idades = reduce(lambda aci, x: x['idade'] + aci, pessoas, 0)
print(f'A soma das idade é {soma_idades}')
media_idade = soma_idades / len(pessoas)
print(f'A media de idade é {media_idade}')

















