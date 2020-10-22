
# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
#Na função 'seek()':
#os argumentos verificam a posição inicial do cursor e ate onde ele vai..
#se caso segundo argumento for 0, ele irar percorrer o arquivo.
# file.seek(0, 0)
#
#
# print('Lendo linhas:')
# print(file.read())
# print('###############')
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print('#########################')
#
# file.seek(0, 0)
# '''.readlines transforma os elementos lidos numa lista'''
# print(file.readlines())
#file.close()

#Em outras linguagens, pode-se trabalhar com 'arquivos'
#usando blocos de 'try/finally'.
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha!!!')
#     file.seek(0,0)
#     print(file.read())
# finally:
#     file.close()

#A maneira mais PYTHON de se trabalhar com 'ARQUIVOS' é:
#USANDO O GERENCIADOR DE CONTEXTO: ele abri o arquivo, e ele mesmo fecha o arquivo.

# with open('nomes.txt', '+w') as file:
#     file.write('ell\n')
#     file.write('beta\n')
#     file.write('pixuleco\n')
#     file.write('sofia')
#
#     file.seek(0)
#     print(file.read())
#     file.seek(0)
#     print(file.readlines())

with open('abc.txt','a+') as file:
    file.write('mariano batista\n')
    file.seek(0)
    print(file.read())





