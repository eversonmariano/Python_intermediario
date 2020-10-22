#1

# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
#
# saudacao('oi', 'ell')
# saudacao('bom dia', 'beta!')

#2
# def soma(n1, n2, n3):
#     print(n1+n2+n3)
#
# soma(2,3,5)
# soma(2,1,2)
# soma(2,2,2)

#3
# def val_percent(val, percent):
#     return val + (val * percent/100)
#
# ap = val_percent(100,15)
# print(ap)
# ap = val_percent(10,2)
# print(ap)
# ap = val_percent(200,50)
# print(ap)

#4
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n

print(fb(8))











