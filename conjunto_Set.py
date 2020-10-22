#add ADICIONA, UPDATE ATUALIZA, CLEAR, DISCARD
#UNION | UNE
#INTERSECTION & TODOS OS ELEMENTOS PRESENTES NOS DOIS SETS
#DIFFERENCE - ELEMENTROS APENAS NO SET DA ESQUERDA
#SYMMETRIC_DIFFERENCE ^ ELEMENTOS QUE ESTAO NOS DOIS SETS, MAS NAO EM AMBOS

s1 = {1,2,3,4,5} #nao existe indice, porem posso fazer iterações.
print(s1, type(s1))

#s1 = {} # isso é um dicionario

#se eu quero criar um set vazio eu uso a funão set()
s2 = set()
s2.add(10)
s2.add(20)
s2.add((40,50,60,'ell'))
print(s2)
s2.discard(20)
print(s2)
s3 = set()
s3.update([6,8,9,9,9,9,23,50,20,40,10,1,2,2,5,6], {9,96,45,10},'PYTHON')
print(s3)
#os sets nao respeitam ordem. pouco importa! eh algo aleatorio.
s4 = list(s3)
print(s4)

s5 = {1,2,3,4,5,10}
s6 = {1,2,3,4,5,6,7,8}
s7 = s5 | s6 #uniao os dois sets
print(s7)
s8 = s5 & s6 #interseçao
print(s8)
s9 = s5 - s6 #diferença apenas no set da esquerda no caso o s5.
print(s9)
s10 = s5 ^ s6 #diferença simetrica
print(s10)

s11 = ['ell', 'beta', 'maria','luiz'] #lista
s12 = ['ell','ell','ell','ell', 'beta', 'maria','beta','beta','beta','luiz'] #lista
print(s11==s12)

s11 = set(s11) #convertendo pra set
s12 = set(s12) #convertendo pra set
print(s11==s12)












