#function that takes factors, multiplies them and checks if they are divisible by 1...20
#returns true or false


def get_prod(r):
    i = 1
    for item in r:
        i *= item
    return i

def check_prod(r):
    print "Checking " + str(r)
    prod = get_prod(r)
    ran = range(1,21)
    for item in ran:
        if prod % item != 0:
            print "Not divisible"
            return False
    print "Divisible"
    return True


r = range(1,21)
rev = list(reversed(r))


for i in rev:
    r2 = r.remove(i)
    print "Iteration: " + str(i)
    print "r2: " + str(r2)
    if check_prod(r) == False:
        r.append(i)
    
    raw_input("Press any key to continue")

print get_prod(r)



    

