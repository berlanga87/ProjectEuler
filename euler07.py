import math

n = int(10001*math.log(10001) + 10001*math.log(math.log(10001))) + 1

r = range(3,n)

lista = [2]

for item in r:
    primality  = True
    for prime in lista:
        if item % prime == 0:
            primality = False
    if primality == True:
        lista.append(item)


print lista[10000]
