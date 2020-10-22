'''
DICIONARIOS
'''

# d1 = {'chave':'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'

# d1 = dict(cha1='val da cha1', cha2='val cha2')
# d1 = {1: 'val cha1', 2: 'val cha2', 3: 'val cha3'}
#
# print(d1)
# print(d1[3])
# print(d1[2])
# print(d1[1])


# d1 = {
#     'str' : 'valStr',
#     123 : 'Val123',
#     (1,2,3,4) : 'Tupla',
# }
#
# print(d1)
# print(d1[(1,2,3,4)])
# print(d1[123])
# print(d1['str'])
# print(d1.get(123))
# d1[123] = 'atualizaValor'
# print(d1[123])
# d1['nova_chave1'] = 'Valor da nova chave1' #adicionando uma novo elemento ao dict
# print(d1)
# d1.update({'nova_chave2':'novo_valor2'}) #adicionando uma novo elemento ao dict
# print(d1)
# print('str' in d1) #checa se o dicionario 'd1' se contem a chave 'str'
# print(123 in d1.keys()) #checa se o dicionario 'd1' se contem a chave 123
# print('Tupla' in d1.values()) #checa se o dicionario 'd1' se contem o valor 'Tupla'
#
# print(len(d1))
#
# for k in d1: #acessara APENAS as chaves
#     print(k)
#
# for v in d1.values(): #acessara APENAS os valores
#     print(v)
#
# for c in d1.items(): #acessara as chaves e os valores, respectivamente
#     print(c)
# for c in d1.items(): #acessara as chaves e os valores, respectivamente
#     print(c[0], c[1], sep=':')
# for c, v in d1.items(): #acessara as chaves e os valores, respectivamente
#     print(c, v, sep=' ,')

#DICIONARIO DENTRO DE DICIONARIO
# clientes = {
#     'Cliente_1': {
#         'nome': 'Ell',
#         'Sobrenome' : 'Mariano',
#     },
#     'Cliente_2': {
#         'nome': 'Beta',
#         'Sobrenome' : 'Mariano',
#     },
#     'Cliente_3': {
#         'nome': 'Snoopy',
#         'Sobrenome': 'Mariano',
#     },
# }

#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# import copy
#
# d1 = {1: 'a', 2: 'b', 3: 'c','d' : ['ell', 'mariano']}
# print(f'd1={d1}')
# v = copy.deepcopy(d1) #permite alteraçao do dicionario, pois foi criada uma copia rasa do dicionario d1
# print(f'v={v}')
#
# v['e'] = 'Beta'
# v['d'][0] = 'Snoopy'
#
# print(d1)
# print(v)

#TRANSFORMANDO UMA LISTA EM DICIONARIO (FAZENDO UM CAST)

# lista = [
#     ['c1',1],
#     ['c2',2],
#     ['c3',3],
# ]
# d1= dict(lista)
# print(d1)
# print(d1['c3'])
#
# #TRANSFORMANDO  Tuplas EM DICIONARIO (FAZENDO UM CAST)
# lista2 = [
#     ('c1',1),
#     ('c2',2),
#     ('c3',3),
# ]
# d2= dict(lista2)
# print(d2)
# print(d2['c1'])
#
# lista3 = (
#     ('c1',1),
#     ('c2',2),
#     ('c3',3),
# )
# d3= dict(lista3)
# print(d3)
# print(d3['c2'])

#FUNÇAO POP

d1 = {
    1: 50,
    2: 200,
    3: 66,
}
print(d1)
# d1.pop(2)#elimina pela chave, valor o elemento do dict
# print(d1)
# d1.popitem() #elimina o ultimo item(chave/valor) do dicionario
# print(d1)

#CONCATENANDO DICIONARIO
d2 = {
    4: 570,
    5: 1150,
    6: 99,
}
print(d2)

d1.update(d2)
print(d1)




