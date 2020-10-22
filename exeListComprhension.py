#TRANSFORMAR A VARIAVEL ABAIXO 'STRING' EM '0123456789.0123456789.012...' USANDO 'COMPREENSAO DE LISTAS'.

string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
step = 10
contador = [x for x in range(0,len(string),step)]
print(contador)
tuplas = [(x,x+step) for x in range(0,len(string), step)]
print(tuplas)
fatiamento = [string[x:x+step] for x in range(0,len(string), step)]
print(fatiamento)
junçao = '.'.join(fatiamento)
print(junçao)

# string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
# nStep = 10
# contador = [i for i in range(0, len(string), nStep)]
# print(contador)
# IniFimTupla = [(i, i+nStep) for i in range(0,len(string), nStep)]
# print(IniFimTupla)
# fatiamento = [string[i:i+nStep] for i in range(0,len(string), nStep)]
# print(fatiamento)
# junçao = '.'.join(fatiamento)
# print(junçao)