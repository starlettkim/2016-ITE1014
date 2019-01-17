import random

guessesTaken = 0

print('Hello! What is your name?')
myName = raw_input()

number = random.randint(1, 20)
print('Well, ' + myName + '. I am thinking of a number between 1 and 20')

while guessesTaken < 6:
	print('Take a guess.')
	guess = int(raw_input())

	guessesTaken = guessesTaken + 1
	if guess < number:
		print('Your guess is too low.')
	elif guess > number:
		print('Your guess is too high.')
	else:
		break

if guess == number:
	print('Good job. ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' times.')
else:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number)
