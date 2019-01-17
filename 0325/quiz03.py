
def pibo(a):
	if (a == 1):
		return 0
	if (a == 2):
		return 1
	return pibo(a-1) + pibo(a-2)

input = raw_input('input: ')
input = int(input)
i = 1
while (i <= input):
	print(pibo(i))
	i+=1