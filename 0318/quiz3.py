

while (1):
	input=raw_input('Input number (End number=0): ')
	input=int(input)
	if input==0:
		print('End number')
		break
	if input%2==0:
		print('Even number')
	else:
		print('Odd number')