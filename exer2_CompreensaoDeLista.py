carrinho = []
carrinho.append(('prod1', 25.5))
carrinho.append(('prod2', 50.5))
carrinho.append(('prod3', 10.5))
carrinho.append(('prod4', 5.5))
print(carrinho)

# clone = [(x, y) for x, y in carrinho]
# print(clone)
# apenasY = [y for x, y in carrinho]
# print(apenasY)
somaY = sum([float(y) for x, y in carrinho])
print(f'Valor Total dos produtos é: {somaY}.')

# carrinho = []
# carrinho.append(('Produto1', '120'))
# carrinho.append(('Produto2', 100))
# carrinho.append(('Produto3', 50))
#
# print(carrinho)
#
# #FAZER UM CLONE DO CARRINHO
#
# cloneCarrinho = [(x, y) for x, y in carrinho]
# print(cloneCarrinho)
#
# #SOMAR APENAS OS VALORES
#
# SomaDosValores = sum([float(y) for x, y in carrinho])
# print(SomaDosValores)