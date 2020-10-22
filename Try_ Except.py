# try:
#     print(a)
# except:
#     print("erro!")

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro!')
except NameError as erro:
    print("Tipo do erro:", erro)
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu codigo foi exexutado com sucesso.')
finally:
    print('O finally sempre será executado!')

print('Bora continuar!')