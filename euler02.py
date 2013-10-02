def get_fibo(max):
				l = [1,2]
				i = 1
				a = True
				# while number is less or equal to max, add fibonacci to list
				while a == True:
								num = l[i]+l[i-1]
								if num <= max:
												l.append(num)
												i += 1
								else:
												a = False
				return l

lista = get_fibo(4000000)

counter = 0
for item in lista:
				if item % 2 == 0:
						print "item = " + str(item)
						counter += item
						print "Counter = " + str(counter)
						print '\n'
print counter						

