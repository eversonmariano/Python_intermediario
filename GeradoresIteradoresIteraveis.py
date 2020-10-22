import sys
import time

# def gera():
#     r = []
#     for i in range(100):
#         yield i
#         time.sleep(0.1)
#     return r
#
# g = gera()

# for v in g:
#     print(v)
l1 = [x for x in range(10000)]
print(type(l1))
l2 = (x for x in range(10000)) #gerador
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))