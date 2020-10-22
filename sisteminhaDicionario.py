print()
print("****************ESCOLHA UMA RESPOSTA CERTA!****************")
print()
perguntas = {
    'Pergunta_1': {
        'pergunta': 'Quanto é 8*7? ',
        'respostas': {'a': '58','b': '56','c': '57',},
        'resp_certa': 'b',
    },
    'Pergunta_2': {
        'pergunta': 'Quanto é 9*9? ',
        'respostas': {'a': '81','b': '105','c': '49',},
        'resp_certa': 'a',
    },
    'Pergunta_3': {
        'pergunta': 'Quanto é 7*5? ',
        'respostas': {'a': '25','b': '45','c': '35',},
        'resp_certa': 'c',
    },
    'Pergunta_4': {
        'pergunta': 'Quanto é 9*7? ',
        'respostas': {'a': '52','b': '45','c': '63',},
        'resp_certa': 'a',
    },
    'Pergunta_5': {
        'pergunta': 'Quanto é 125*8? ',
        'respostas': {'a': '1200','b': '1005','c': '1000',},
        'resp_certa': 'c',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items(): #ACESSA A CHAVE E O VALOR DAS PERGUNTAS DO DICIONARIO
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items(): #ACESSA AS RESPOSTAS (CHAVE E O VALOR) DO DICIONARIO
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Qual é a sua resposta? ')

    if resposta_usuario == pv['resp_certa']:
        print('OK, VOCÊ ACERTOU!!!!')
        respostas_certas += 1
    else:
        print('QUE PENA, VOCÊ ERROU!!!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'VOCÊ ACERTOU {respostas_certas} resposta(as)!!!')
print(f'SEU PERCENTUAL DE ACERTOS FOI {porcentagem_acerto}%.')


print()