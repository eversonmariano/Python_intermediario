
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1] #faz uma copia exata de l1

ex2 = [v * 2 for v in l1] #multiplica cada elemento por 2
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['ella', 'beta', 'maria']
ex4 = [v.replace('a','@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(x, y) for x, y in tupla]#('chave','valor')
ex6 = [(y, x) for x, y in tupla] #inverte ('valor', 'chave')
ex7 = dict(ex6) #converteu ex6 num dicionario
print(ex7)


l3 = list(range(100)) #lista de 0 a 99
ex8 = [v for v in l3 if v % 5 == 0 if v % 8 == 0] #obtenho todos os divisores de 5 em l3
print(ex8)

ex9 = [v if v % 2 == 0 else 'não é div por 2' for v in l3] #todos os divisiveis por 2 aparecerao, caso contrario aparecera a mensagem do else.

print(ex9)

ex10 = [v if v % 4 == 0 and v % 7 == 0 else 0 for v in l3] #divisiveis por 4 e 7
print(ex10)

















