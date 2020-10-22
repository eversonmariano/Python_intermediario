#https://docs.python.org/3/library/exceptions.html


#def divide(n1: int, n2: int) -> float:
# def divide(n1, n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise
#
# #com o raise vc pode relançar uma excessao.
#
# try:
#     print(divide(3,0))
# except ZeroDivisionError as error:
#     print(error)

'''
Criando minha propria excessão
'''

def divide(n1, n2):
    if n2 == 0:
        raise ValueError(" n2 não pode ser ZERO!")
    return n1/n2

try:
    print(divide(2, 0))
except ValueError as erro:
    print("Não divida por zero!")
    print('Log:',erro)