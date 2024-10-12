from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(3000)
@lru_cache()
def fact(x):
    if x==1:
        return 1
    return x*fact(x-1)

for i in range(1, 12312+1):
    fact(i)

print(fact(1232))

