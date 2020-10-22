'''TUPLAS - NAO PODEMOS EDITAR OS ELEMENTOS DA TUPLA.
ESSA É A DIFERENÇA ENTRE TUPLA E LISTAS'''

t1 = (1,2,3,'a','ell mariano')
t2 = 1,2,3,'a','ell mariano'
t3 = 1,
t4 = (1,2,3,'a','ell mariano') * 10 #repete a tupla 'n' vezes
t5 = (1,2,3,'a','ell mariano')
t5 = list(t5) #converte tupla em lista


print(t1)
print(t1[2:])
print(t4)
print(t5)