from itertools import groupby

alunos = [
    {'nome': 'Ell', 'nota':'A'},
    {'nome': 'Beta', 'nota':'B'},
    {'nome': 'leo', 'nota':'C'},
    {'nome': 'maria', 'nota':'C'},
    {'nome': 'jose', 'nota':'D'},
    {'nome': 'paulo', 'nota':'A'},
    {'nome': 'tiago', 'nota':'B'},
    {'nome': 'pedro', 'nota':'D'},
    {'nome': 'amanda', 'nota':'C'},
    {'nome': 'roberto', 'nota':'B'},

]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

# for agrupamento, valor_agrupado in alunos_agrupados:
#     print(f'Agrupamento: {agrupamento}')
#     for aluno in valor_agrupado:
#         print(aluno)
#     print()
for agrupamento, valor_agrupado in alunos_agrupados:
    qtd = len(list(valor_agrupado))
    print(f'{qtd} alunos tiraram a nota {agrupamento}')

    