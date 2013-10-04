import time
def is_palindrome(n):
    n = list(str(n))
    length = len(n)
    mid = length/2
    if len(n) % 2 == 0:
        if n[0:mid] == list(reversed(n[mid:])):
            return True
        else:
            return False
    else:
        if n[0:mid] == list(reversed(n[mid+1:])):
            return True
        else:
            return False


def find_palindrome(list):
    list2 = []
    for num in list:
        if is_palindrome(num):
            list2.append(num)
    return list2


i = range(100,999)
j = i

lista = []
for item1 in i:
    for item2 in j:
        lista.append(item1*item2)

lista = list(set(lista))
lista = list(reversed(lista))

start = time.time()
p = max(find_palindrome(lista))
elapsed = (time.time() - start)
print "the algorithm took %s seconds" % elapsed
print "the result is: %s" % p
