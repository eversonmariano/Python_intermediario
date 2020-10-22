'''EXPRESSOES LAMBDAS (OU FUNÇOES ANONIMAS)'''

# a = lambda x, y: x * y
# print(a(2, 10))

lista = [
    ['p1', 13],
    ['p2', 8],
    ['p3', 75],
    ['p4', 50],
    ['p5', 170],
]
# def func(item):
#     return item[1]
#
# lista.sort(key=func, reverse=True) //ORDENANDO LISTA NA ORDER DECRESCENTE DE VALORES
# print(lista)
#lista.sort(key=lambda item: item[1]) #ORDENANDO LISTA NA ORDER CRESCENTE DE VALORES
print(sorted(lista, key=lambda i: i[1], reverse=True)) #ORDENANDO LISTA NA ORDER DECRESCENTE DE VALORES