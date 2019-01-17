

count=0
i=1
while i<=100:
	div=i/10
	if i-div*10==3:
		print(i)
		count=count+1
	elif i-div*10==6:
		print(i)
		count=count+1
	elif i-div*10==9:
		print(i)
		count=count+1
	i=i+1
print('count= '+str(count))