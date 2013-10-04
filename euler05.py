#function that takes factors, multiplies them and checks if they are divisible by 1...20
#returns true or false
import time

def get_prod(r):
    i = 1
    for item in r:
        i *= item
    return i

def check_prod(r):
    prod = get_prod(r)
    ran = range(1,21)
    for item in ran:
        if prod % item != 0:
            return False
    return True

start = time.time()
r = range(1,21)
rev = list(reversed(r))


for i in rev:
    r2 = r.remove(i)
    if check_prod(r) == False:
        r.append(i)
    

print get_prod(r)
print 'Time to finish: ' + str(time.time() - start)
