
def func(input):
	i=1
	while i<10:
		print(str(input) + ' * ' + str(i) + ' = ' + str(input*i))
		i=i+1

input=raw_input()
input=int(input)
func(input)