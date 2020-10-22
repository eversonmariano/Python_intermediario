'''
CONSIDERANDO DUAS LISTAS DE INTEIROS OU FLOATS (LISTA A E LISTA B),
SOME OS VALORES NAS LISTAS RETORNANDO UMA NOVA LISTA COM OS VALORES SOMADOS.

SE UMA LISTA FOR MAIOR QUE A OUTRA, A SOMA SÓ VAI CONSIDERAR O TAMANHO DA MENOR.
EXEMPLO:
LISTA_A = [1,2,3,4,5,6,7]
LISTA_B = [1,2,3,4]
-----------
RESULTADO = [2,4,6,8]
'''

lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4]

soma = [x + y for x, y in zip(lista_A, lista_B)]
print(soma)

# for i in range(len(lista_B)):
#     soma.append(lista_A[i] + lista_B[i])
# print(soma)

#UMA MANEIRA MAIS PYTHONICA DE FAZER O RESULTADO.
# for i, _ in enumerate(lista_B):
#     soma.append(lista_A[i] + lista_B[i])
# print(soma)

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]