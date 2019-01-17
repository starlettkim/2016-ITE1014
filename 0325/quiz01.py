
def calc(a,b,c):
	if (b == '+'):
		return a+c
	if (b == '-'):
		return a-c
	if (b == '*'):
		return a*c
	if (b == '/'):
		return a/c

a = raw_input('1st: ')
b = raw_input('operator: ')
c = raw_input('2nd: ')
print(a + b + c + '=' + str(calc(int(a), b, int(c))))