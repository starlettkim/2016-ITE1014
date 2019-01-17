sum = 50
input = raw_input().split()
for i in range(len(input)):
	if (input[i] == 'bab'):
		sum+=1
	elif (input[i] == 'baby'):
		sum-=2
print(sum)