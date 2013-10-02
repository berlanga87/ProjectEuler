def get_calc(l):
				counter = 0
				for item in l:
								if item % 3 == 0:
												counter += item
								elif item % 5 == 0:
												counter += item
				return counter

lista = range(1,1000)
print get_calc(lista)
