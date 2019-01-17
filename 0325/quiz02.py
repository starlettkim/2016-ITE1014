
def calc(a, b):
	i = a
	while (i <= b):
		j = 1
		while (j <= 9):
			print('%d * %d = %d'%(i,j,i*j))
			j+=1
		i+=1

a = raw_input('1st: ')
b = raw_input('2nd: ')
calc( int(a), int(b) )