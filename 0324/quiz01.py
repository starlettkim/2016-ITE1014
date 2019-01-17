
def fac(input):
	if (input == 1):
		return 1
	return input * fac(input - 1)

input = raw_input()
input = int(input)
print(fac(input))