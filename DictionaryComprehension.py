# lista = [('chave','valor'), ('chave1','valor1'), ('chave2','valor2')]
# print(lista)

#transformando a lista de tuplas num dicionario via compreensao de dicionarios

# d1 = {k: v for k, v in lista}
# print(d1)
# d1 = {k.upper(): v.upper() for k, v in lista}
# print(d1)
d1 = {k: v for k, v in enumerate(range(5))}
print(d1, type(d1))

d3 = {f'chave_{k}': k*10 for k in range(5)}
print(d3, type(d3))




#PARA SE FORMAR UM SET(CONJUNTOS)
# d2 = {k for k in range(6)}
# print(d2, type(d2))
