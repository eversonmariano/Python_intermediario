# import os
#
# os.remove('abc.txt') //APAGA O ARQUIVO abc.txt

'''MANIPULANDO ARQUIVO JASON'''
import json
#dicionario
d1 = {
    'Pessoa 1': {
        'nome': 'ell',
        'idade': 37,
    },
    'Pessoa 2': {
        'nome': 'beta',
        'idade': 42,
    },
}


#Convertendo para arquivo jason

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)