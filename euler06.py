import time
def sum_sq(r):
    i = 0
    for item in r:
        i += item*item
    return i

def sq_sum(r):
    i = 0
    for item in r:
        i += item
    return i*i

start = time.time()
l = range(1,101)
print str(l)
print "Result: " + str(sq_sum(l)-sum_sq(l))
print "Time: " + (str(time.time()-start))
