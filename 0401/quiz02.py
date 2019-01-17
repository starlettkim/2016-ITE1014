alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
count = int(raw_input('Number count: '))
sum = 0
for i in range(count):
	input = raw_input('alp: ')
	for j in range(26):
		if input == alpha[j] :
			sum += num[j]	
print (sum)