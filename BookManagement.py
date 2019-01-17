# -*- coding: utf-8 -*-
# Above line declares encoding type as utf-8.

'''
Book Management System v1.0
Copyright (c) 2016 Jihun Kim. All rights reserved.

!! PLEASE READ ReadMe.txt !!

'''

# Import 'time' module to use sleep(n) method.
import time
# Import 'os' module to use system('') method.
import os
# Import 'random' module to use randint(n,m) method.
import random

# ID number of logined account.
currentAccount = 0

# Dictonary that stores user list.
# {IDNumber:[ID,PW,Name,State]}
# State: 0-invalid, 1-valid
userList = {}

# Dictonary that stores book list.
# {BookNumber:[BookName,Author,Publisher,PublishYear,State]}
# State: IDNumber of user who borrowed this book.
bookList = {}

# Function that loads files.
def fileLoad():
	# Print that system is loading files.
	print '\nLoading files...',

	# Open UserList.dat file as read only mode.
	userListFile = open('./data/UserList.dat', 'r')
	# Repeat this block until meet EOF (End of file)
	while True:
		# Read a single line, make it a list, and store it to temporary list 'tmp'.
		tmp = userListFile.readline().split()
		# If meet EOF, break this loop
		if not tmp: break
		# Add key which is equal to ID number, and make the value a list.
		userList[int(tmp[0])] = []
		# Repeat this block.
		for i in range(1,5):
			# Add data to the value list
			userList[int(tmp[0])].append(tmp[i])
		
	# Open BookList.dat file as read only mode.
	bookListFile = open('./data/BookList.dat', 'r')
	# Repeat this block until meet EOF (End of file)
	while True:
		# Read a single line, make it a list, and store it to temporary list 'tmp'.
		tmp = bookListFile.readline().split()
		# If meet EOF, break this loop
		if not tmp: break
		# Add key which is equal to book number, and make the value a list.
		bookList[int(tmp[0])] = []
		# Repeat this block.
		for i in range(1,6):
			# Add data to the value list
			bookList[int(tmp[0])].append(tmp[i])

	# Print that system finished loading files.
	print ' Done.\n'
	# Close files.
	userListFile.close()
	bookListFile.close()

# Function that stores files.
# If option is 0, store user list.
# If option is 1, store book list.
def fileStore(option):
	if option == 0:
		# Print that program is saving user list file.
		print '\nSaving user list file...',
		# Open UserList.dat file as write mode.
		userListFile = open('./data/UserList.dat', 'w')

		# Repeat to write all user's information.
		for i in userList:
			# Write user's information on user list file.
			userListFile.write(str(i)+' '+userList[i][0]+' '+userList[i][1])
			userListFile.write(' '+userList[i][2]+' '+userList[i][3]+'\n')

		# Close user list file.
		userListFile.close()

	if option == 1:
		# Print that program is saving book list file.
		print '\nSaving book list file...',
		# Open BookList.dat file as write mode.
		bookListFile = open('./data/BookList.dat', 'w')

		# Repeat to write all informations of book.
		for i in bookList:
			# Write information of book on book list file.
			bookListFile.write(str(i)+' '+bookList[i][0]+' '+bookList[i][1])
			bookListFile.write(' '+bookList[i][2]+' '+bookList[i][3])
			bookListFile.write(' '+bookList[i][4]+'\n')

		# Close book list file.
		bookListFile.close()

	# Print that system finished saving files.
	print ' Done.'

# Function that clears screen
def cls():
	# Use cls command.
	os.system('cls')

# Function that finishes program.
def exitProgram():
	# Clear screen.
	cls()
	print '=== [ Exit Program ] ===\n'
	# Repeat until get valid input.
	while True:
		print 'Do you really want to exit this program? (y/n)'
		select = raw_input('>> ')

		# If user choosed 'n' or 'N'
		if select in ['n','N']:
			# Exit this function.
			return

		# If user choosed 'y' or 'Y' 
		elif select in ['y','Y']: 
			# Exit this program.
			exit()

		# If user input is invalid, print that input is invalid.
		print 'Invalid input. You have to enter \'y\' or \'n\'.'

# Function that encrypts given string and return it.
def encrypt(input):
	# Return encrypted input
	return input

# Function that check inputID whether exist
# If exist, return ID number of inputID.
def checkID(inputID):
	# Variable that stores ID number of input.
	inputIDNumber = 0

	# Variable i points ID number.
	for i in userList:
		# If ID input is in user list
		if inputID == userList[i][0]:
			# Store IDNumber
			inputIDNumber = i
			# ..and break
			break

	# Return ID number of inputID.
	return inputIDNumber

# Function that handles login operation.
def login():
	# Clear screen.
	cls()
	# Print login screen.
	print '\n\n\n                     ______ Login ______\n'
	print '\n   If you enter wrong PW 5 times, account will be locked.'
	print '          If you want to quit this menu, enter 0.          \n'

	inputIDNumber = 0

	# Repeat until ID is existing and valid.
	while True:
		# Get ID input.
		inputID = raw_input('                     ID: ')

		# If input is '0'
		if inputID == '0':
			# Exit this function.
			return

		# Call checkID function, and get ID number of input.
		inputIDNumber = checkID(inputID)

		# If input ID doesn't exist
		if not inputIDNumber:
			# Print that user ID doesn't exist.
			print '            That ID doesn\'t exist. Try another.\n'

		# If account is invalid
		elif userList[inputIDNumber][3] == '0':
			print '                That user is unable to login.'
			print '            Need to wait for admin\'s permission.'

		# If ID is existing and valid, break
		else: break
		
	# Count password input errors.
	errorCount = 0
	# Repeat until PW is right
	while True:
		# Get PW input.
		inputPW = raw_input('                     PW: ')

		# If input is '0'
		if inputPW == '0':
			# Exit this function.
			return

		# If encrypted PW input is equal to stored PW of user
		if encrypt(inputPW) == userList[inputIDNumber][1]:
			# Use currentAccount variable as global variable.
			global currentAccount
			# ID number of input is now current account number.
			currentAccount = inputIDNumber
			# Print that user logined successfully.
			print '                     Login successful.'
			# Pause.
			os.system('pause')
			# Exit login function.
			return

		# If password is wrong, increase errorCount.
		errorCount += 1
		# Print that the password is wrong.
		print '            You entered wrong password %d times.\n'%errorCount
		# If user entered wrong password 5 times
		if errorCount == 5:
			# If input ID is Admin
			if inputIDNumber == 1:
				# Print that user failed login.
				print '                Login failed. Wait a moment.'
				# Sleep a moment to prevent brute force attack.
				time.sleep(3)
				# Clear screen.
				cls()
				# Exit login function.
				return

			# If input ID is not Admin
			# set account invalid.
			userList[inputIDNumber][3] = '0'
			# Store userList file.
			fileStore(0)
			# Print that account is locked.
			print '             Account locked. Contact to admin.'
			# Pause.
			os.system('pause')
			# Clear screen.
			cls()
			# Exit login function.
			return

# Function that handles logout operation.
def logout():
	# Use 'currentAccount' variable as a global variable.
	global currentAccount
	# Make user a guest user.
	currentAccount = 0

# Function that handles signup operation.
def signUp():
	# Clear screen.
	cls()
	# Print signup menu.
	print '=== [ Signup ] ===\n'
	print 'If you want to quit this menu, enter 0.\n'

	# Repeat until user ID input is valid.
	while True:
		# Get user's ID input.
		inputID = raw_input('>> ID: ')

		# If user entered '0'
		if inputID == '0':
			# Exit this function.
			return

		# If user's input is too short
		if len(inputID) < 3:
			# Print that input is invalid.
			print 'Invalid input. Length of ID must be 3~16.'

		# If user's input is too long.
		elif len(inputID) > 16:
			# Print that input is invalid.
			print 'Invalid input. Length of ID must be 3~16.'

		# If user's input contains blank
		elif ' ' in inputID:
			# Print that ID is invalid.
			print 'Invalid input. ID must not contain blank.'

		# If user's ID input isn't exist in user list, break this loop.
		elif not checkID(inputID): break

		# If user's ID input is exist in user list
		else:
			# Print that ID already exists.
			print 'That ID already exists. Try another.'

	# Repeat until user PW input is valid.
	while True:
		# Get user's PW input.
		inputPW = raw_input('>> PW: ')

		# If user entered '0'
		if inputPW == '0':
			# Exit this function.
			return

		# If user's input is too short
		if len(inputPW) < 3:
			# Print that PW is too short.
			print 'Invalid input. Length of PW must be 3~16.'

		# If user's input is too long
		elif len(inputPW) > 16:
			# Print that PW is too long.
			print 'Invalid input. Length of PW must be 3~16.'

		# If user's input contains blank
		elif ' ' in inputPW:
			# Print that PW is invalid.
			print 'Invalid input. PW must not contain blank.'

		# If user's input is valid, break this loop.
		else: break

	# Repeat until user name input is valid.
	while True:
		# Get user's name input.
		inputName = raw_input('>> Name: ')

		# If user entered '0'
		if inputName == '0':
			# Exit this function.
			return

		# If input is too short
		if len(inputName) < 2:
			# Print that name is too short.
			print 'Invalid input. Length of name must be 2~16.'

		# If input is too long
		elif len(inputName) > 16:
			# Print that name is too long.
			print 'Invalid input. Length of name must be 2~16.'


		# If user's input contains blank
		elif ' ' in inputName:
			# Print that name is invalid.
			print 'Invalid input. Name must not contain blank.'

		# If user's input is valid, break this loop.
		else: break

	# Allocate ID number for a new user.
	# (Last ID Number of UserList + 1) is a ID Number for a new user.
	newUserIDNumber = userList.keys()[len(userList)-1] + 1
	# Make a list in userList.
	userList[newUserIDNumber] = []
	# Store ID.
	userList[newUserIDNumber].append(inputID)
	# Store PW.
	userList[newUserIDNumber].append(inputPW)
	# Store name.
	userList[newUserIDNumber].append(inputName)
	# User's state is invalid.
	userList[newUserIDNumber].append('0')
	# Store file.
	fileStore(0)

	# Print that Signup is succeeded.
	print 'Congratulations. Signup has succeeded.'
	print 'But you can\'t use this account before admin\'s permission.'
	# Pause.
	os.system('pause')
	# Clear screen.
	cls()

# Function that prints all books.
def bookPrint():
	# Change window size.
	os.system('mode con: cols=82 lines=%s' % (len(bookList) + 10))
	# Print bookPrint screen.
	print '\n === [ Print all books ] ===\n'

	# If current account is admin
	if currentAccount == 1:
		print '\'State\' is ID number of user who borrowed that book.\n'

	else:
		print '\'State\' is Y when you can borrow that book, and N when you can\'t.\n'

	print ' Number |          Book Name         |     Author    |    Publisher  |Year|State'
	# Repeat to print all books.
	for i in bookList:
		# Print informations of books.
		print '%8s|%28s|%15s|%15s|%4s|'%(i,bookList[i][0],bookList[i][1],bookList[i][2],bookList[i][3]),

		# 'state' contains a information of userID.
		# So, to protect personal data, print 'state' when only currentAccount is admin.

		# If current account is admin, print the number of ID.
		if currentAccount == 1: print '%5s'%bookList[i][4]

		# If current account is guest or user
		else:
			# If nobody borrowed this book, print 'Y'.
			if bookList[i][4] == '0': print '  Y  '
			# If someone borrowed this book, print 'N'.
			else: print '  N  '
		
	print '\nDone.'
	# Pause.
	os.system('pause')
	# Clear screen.
	cls()

# Function that searches the book.
def bookSearch():
	# Change window size.
	os.system('mode con: cols=82 lines=30')

	# Repeat until user wants to quit this menu.
	while True:
		# Clear screen.
		cls()
		# Print search the book menu.
		print '=== [ Search the book ] ===\n'
		print 'Enter the name of a book you want to search.'
		print 'If you want to quit this menu, enter 0.'
		# Get user's input.
		bookNameInput = raw_input('>> Book name: ')
		# If input is '0'
		if bookNameInput == '0':
			# Exit this function.
			return

		# Make a list to store book numbers.
		bookNumberList = []
		# Repeat to check all books in bookList.
		for i in bookList:
			# If a book name contains string of bookNameInput
			# Use lower() method to ignore case. 
			if bookNameInput.lower() in bookList[i][0].lower():
				# Append a book number to bookNumberList.
				bookNumberList.append(i)

		# If 0 results found
		if not len(bookNumberList):
			print '\nNo result found.'
			# Pause.
			os.system('pause')
			# Skip below codes.
			continue

		# Print a number of results.
		print '\n%d results found.' % len(bookNumberList)
		print '\'State\' is Y when you can borrow that book, and N when you can\'t.'
		print ' Number |          Book Name         |     Author    |    Publisher  |Year|State'
		for i in bookNumberList:
			print '%8s|%28s|%15s|%15s|%4s|'%(i,bookList[i][0],bookList[i][1],bookList[i][2],bookList[i][3]),
			# If nobody borrowed this book
			if bookList[i][4] == '0':
				# Print 'Y'.
				print '  Y  '
			# If someone borrowed this book
			else:
				# Print 'N'.
				print '  N  '

		# If logined account is guest or admin
		if currentAccount in [0,1]:
			# Pause.
			os.system("pause")
			# Skip below codes.
			continue

		print '\nIf you want to borrow a book, enter the book number.'
		print 'Enter 0 if you not want to.'
		# Repeat until user input is valid.
		while True:
			# Get user's input.
			bookNumberInput = raw_input (">> Book number: ")
			# If user entered '0'
			if bookNumberInput == '0':
				# Break this loop.
				break

			# If user's input is not a digit
			if not bookNumberInput.isdigit():
				print 'Invalid input. You must enter a number.'
				# Skip below codes.
				continue

			# Convert type of bookNumberInput variable to int variable.
			bookNumberInput = int(bookNumberInput)

			# If user input is valid
			if bookNumberInput in bookList:
				# If someone already borrowed that book
				if bookList[bookNumberInput][4] != '0':
					# Print that user can't borrow that book.
					print 'Sorry. You can\'t borrow that book. Try another.'

				# If nobody borrowed that book
				else:
					# Call bookBorrow(bookNumberInput) function.
					bookBorrow(bookNumberInput)
					# Exit this function.
					return

			# If book doesn't exists
			else:
				# Print that input is invalid.
				print 'Invalid input. That book doesn\'t exists.'

# Function that inserts new book.
def bookInsert():
	# Clear screen.
	cls()
	# Print insert new book menu.
	print '=== [ Insert new book ] ===\n'
	print 'If you want to quit this menu, enter 0.\n'
	print 'Please input the information of a book.'
	# Repeat until get valid input.
	while True:
		# Get user's input.
		bookNumberInput = raw_input ('>> Book Number: ')

		# If user's input is 0
		if bookNumberInput == '0':
			# Exit this function.
			return

		# If input is not a digit
		if not bookNumberInput.isdigit():
			# Print that input is invalid.
			print 'Invalid input. You must enter a number.'
			# Skip below codes.
			continue

		# If input is too long
		if len(bookNumberInput) > 8:
			# Print that input is invalid.
			print 'Invalid input. Length of the book number must be 1-8.'
			# Skip below codes.
			continue

		# If no input
		if bookNumberInput == '':
			# Print that input is invalid.
			print 'Invalid input. Input something.'
			# Skip below codes.
			continue

		# Convert type of bookNumberInput variable to int variable.
		bookNumberInput = int(bookNumberInput)

		# If user input is valid
		if bookNumberInput not in bookList:
			# Break this loop.
			break

		# If user input is invalid, print that input is invalid.
		print 'Invalid input. That book number already exists.'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		bookNameInput = raw_input ('>> Book Name: ')

		# If user's input is 0
		if bookNameInput == '0':
			# Exit this function.
			return

		# If input is too long
		if len(bookNameInput) > 28:
			# Print that input is invalid.
			print 'Invalid input. Length of the book name must be 1-28.'
		# If no input
		elif bookNameInput == '':
			# Print that input is invalid.
			print 'Invalid input. Input something.'

		# If bookNameInput doesn't contain blank
		elif not ' ' in bookNameInput:
			# Break this loop.
			break

		# If not
		else:
			# Print that input is invalid.
			print 'Invalid input. Book name must not contain blank.'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		authorInput = raw_input ('>> Author: ')

		# If user's input is 0
		if authorInput == '0':
			# Exit this function.
			return

		# If input is too long
		if len(authorInput) > 15:
			# Print that input is invalid.
			print 'Invalid input. Length of the author must be 1-15.'

		# If no input
		elif authorInput == '':
			# Print that input is invalid.
			print 'Invalid input. Input something.'

		# If authorInput doesn't contain blank
		elif not ' ' in authorInput:
			# Break this loop.
			break

		# If not,
		else:
			# Print that input is invalid.
			print 'Invalid input. Author must not contain blank.'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		publisherInput = raw_input ('>> Publisher: ')

		# If user's input is 0
		if publisherInput == '0':
			# Exit this function.
			return

		# If input is too long
		if len(publisherInput) > 15:
			# Print that input is invalid.
			print 'Invalid input. Length of the publisher must be 1-15.'

		# If no input
		elif publisherInput == '':
			# Print that input is invalid.
			print 'Invalid input. Input something.'

		# If publisherInput doesn't contain blank
		elif not ' ' in publisherInput:
			# Break this loop.
			break

		# If not
		else:
			# Print that input is invalid.
			print 'Invalid input. Publisher must not contain blank.'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		publsihYearInput = raw_input ('>> Publish Year: ')

		# If user's input is 0
		if publsihYearInput == '0':
			# Exit this function.
			return

		# If input is too long
		if len(publsihYearInput) > 4:
			# Print that input is invalid.
			print 'Invalid input. Length of the publish year must be 1-4.'

		# If no input
		elif publsihYearInput == '':
			# Print that input is invalid.
			print 'Invalid input. Input something.'

		# If input is not a digit
		elif not publsihYearInput.isdigit():
			# Print taht input is invalid.
			print 'Invalid input. Publish year must be a digit.'

		# If publsihYearInput doesn't contain blank
		elif not ' ' in publsihYearInput:
			# Break this loop.
			break

		# If not
		else:
			# Print that input is invalid.
			print 'Invalid input. Author must not contain blank.'

	# Make a list in bookList[bookNumberInput]
	bookList[bookNumberInput] = []
	# Append bookNameInput to the list
	bookList[bookNumberInput].append(bookNameInput)
	# Append authorInput to the list
	bookList[bookNumberInput].append(authorInput)
	# Append publisherInput to the list
	bookList[bookNumberInput].append(publisherInput)
	# Append publishYearInput to the list
	bookList[bookNumberInput].append(publsihYearInput)
	# State is 0
	bookList[bookNumberInput].append('0')
	# Store bookList to a file.
	fileStore(1)

	print 'Book insert done.'
	#Pause.
	os.system('pause')
	# Clear screen.
	cls()

# Function that deletes existing book.
def bookDelete():
	# Clear screen.
	cls()
	# Print delete existing book menu.
	print '=== [ Delete existing book ] ===\n'
	print 'Check book\'s number before delete existing book.'
	print 'If you want to quit this menu, enter 0.\n'
	# Repeat until input is 0.
	while True:
		# Get user's input.
		bookNumberInput = raw_input('>> Book Number: ')

		# If input is 0
		if bookNumberInput == '0':
			# Exit this function.
			return

		# If input is not a digit
		elif not bookNumberInput.isdigit():
			# Print that input is invalid.
			print 'Invalid input. Enter the number of a book.'

		# If input is in bookList
		elif bookNumberInput in bookList:
			# Delete a book in bookList.
			del bookList[bookNumberInput]
			# Store to book list file.
			fileStore(1)
			# Print that deletion is done.
			print 'Book number (%d) deleted successfully.' % bookNumberInput

		# If not
		else:
			# Print that input is invalid.
			print 'Invalid input. That book doesn\'t exist.'

# Function that handles book borrow operation.
def bookBorrow(bookNumber):
	# Count the number of books borrowed by current user.
	count = 0
	# Repeat to check all books in bookList
	for i in bookList:
		# If book state is equal to currentAccount
		if int(bookList[i][4]) == currentAccount:
			# Count.
			count += 1

	# If user already borrowed three books
	if count == 3:
		# Print that user can't borrow more book
		print 'You already borrowed three books.'
		print 'You can\'t borrow more than three books.'
		# Pause.
		os.system('pause')
		# Exit this function
		return

	# Store ID Number of current account to state of a book.
	bookList[bookNumber][4] = str(currentAccount)
	# Store book list file.
	fileStore(1)
	# Print that borrow operation finished successfully.
	print 'You successfully borrowed this book.'
	print '%d: %s by %s.' % (bookNumber, bookList[bookNumber][0], bookList[bookNumber][1])
	# Pause.
	os.system('pause')

# Function that handles book return operation.
def bookReturn():
	# Change window size.
	os.system('mode con: cols=75')
	# Print return the book menu.
	print '\n=== [ Return the book ] ===\n'
	print 'If you want to quit this menu, enter 0.\n'

	# Count the number of books borrowed by current user.
	count = 0
	# Stores book number of book borrowed by current user.
	borrowedBookList = []
	# Repeat to check all books in bookList
	for i in bookList:
		# If book state is equal to currentAccount
		if int(bookList[i][4]) == currentAccount:
			# Count.
			count += 1
			# Store book number.
			borrowedBookList.append(i)

	print 'You borrowed %d book(s).' % count
	print ' Number |          Book Name         |     Author    |    Publisher  |Year'
	for i in borrowedBookList:
		print '%8s|%28s|%15s|%15s|%4s'%(i,bookList[i][0],bookList[i][1],bookList[i][2],bookList[i][3])

	# Repeat until get valid input.
	while True:
		print '\nEnter the book number you want to return.'
		# Get user input.
		returnBookInput = raw_input('>> Book number: ')

		# If user's input is '0'.
		if returnBookInput == '0':
			# Exit this function.
			return

		# If input is not a digit
		if not returnBookInput.isdigit():
			# Print that input is invalid.
			print 'Invalid input. You have to input a number of the book.'

		# If input is not in borrowed book list
		elif int(returnBookInput) not in borrowedBookList:
			# Print that input is invalid.
			print 'Invalid input. You didn\'t borrowed that book.'

		# If input is valid
		else:
			# Break this loop.
			break

	# set book state to 0.
	bookList[int(returnBookInput)][4] = '0'
	# Save file.
	fileStore(1)
	# Print that book return has succeeded.
	print 'Book return succeeded.'
	# Pause.
	os.system('pause')

# Function that permits account unlock request.
def userPermit():
	# Clear screen.
	cls()
	# Print permit account unlock request menu.
	print '\n=== [ Permit account unlock request ] ===\n'

	# Make a list that stores invalid users' ID number.
	invalidUserList = []
	# Repeat to check all users in userList.
	for i in userList:
		# If user's state is '0'(invalid)
		if userList[i][3] == '0':
			# Append that user's ID number in invalidUserList.
			invalidUserList.append(i)

	# If there is nothing in invalidUserList
	if not len(invalidUserList):
		# Print that no result found.
		print '\nNo result Found.'
		# Pause.
		os.system('pause')
		# Exit this function.
		return

	print ' IDNum |        ID        |       Name'
	# Repeat to check all user in invalidUserList.
	for i in invalidUserList:
		print '%6s | %16s | %16s' % (i, userList[i][0], userList[i][2])

	print '\nInput the ID number you want to permit.'
	print 'If you want to quit this menu, enter 0.'
	# Repeat until get valid input.
	while True:
		userIDInput = raw_input ('\n>> ID Number: ')

		# If user input is '0'
		if userIDInput == '0':
			# Exit this function.
			return

		# If input is not a digit
		if not userIDInput.isdigit():
			# Print that input is invalid.
			print 'Invalid input. You have to input a ID Number.'
			# Skip below codes.
			continue

		# Change variable type to integer.
		userIDInput = int(userIDInput)

		# If userIDInput is in invalidUserList
		if userIDInput in invalidUserList:
			# break this loop.
			break

		# If userIDInput is in userList but not in invalidUserList
		elif userIDInput in userList:
			# Print that input is invalid.
			print 'Invalid input. That user is not a invalid user.'

		# If not
		else:
			# Print that input is invalid.
			print 'Invalid input. That user ID doesn\'t exists.'

	# Make user valid.
	userList[userIDInput][3] = '1'
	# Store userList file.
	fileStore(0)
	print 'ID Number: %d\nPermission succeeded.\n' % userIDInput
	# Pause.
	os.system('pause')

# Function that deletes existing user.
def userDelete():
	# Change window size.
	os.system('mode con: cols=47 lines=%s' % (len(userList)+25))
	# Print delete existing user menu.
	print '\n=== [ Delete existing user ] ===\n'
	print 'If you want to quit this menu, enter 0.\n'
	print 'State: 0-invalid, 1-valid.'
	print ' IDNum|       ID       |      Name      |State'

	# Repeat to print all users in user list.
	for i in userList:
		# Print user information.
		print ' %5s|%16s|%16s|%3s' % (i, userList[i][0], userList[i][2], userList[i][3])

	print '\nInput the ID number you want to delete.'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		inputIDNumber = raw_input('>> ID Number: ')

		# If input is '0'.
		if inputIDNumber == '0':
			# Exit this function.
			return

		# If input is not a digit
		if not inputIDNumber.isdigit():
			# Print that input is invalid.
			print 'Invalid input. You must input a ID Number.'

		# If input ID Number doesn't exist in user list
		elif int(inputIDNumber) not in userList:
			# Print that input is invalid.
			print 'Invalid input. That user doesn\'t exists.'

		# If input is valid
		else:
			# Break this loop.
			break

	# Change variable type.
	inputIDNumber = int(inputIDNumber)

	# Print operation choose menu.
	print 'What operation do you want?'
	print '(1) Delete user'
	print '(2) Change user state to invalid'

	# Repeat until get valid input.
	while True:
		# Get user's input.
		operationInput = raw_input('>> ')

		# If user's input is '0'.
		if operationInput == '0':
			# Exit this function.
			return

		# If user's input is invalid
		if operationInput not in ['1','2']:
			# Print that input is invalid.
			print 'Invalid input. Input the number of menu.'

		# If input is valid
		else:
			# Break this loop.
			break

	# If user choosed 'Delete user'
	if operationInput == '1':
		# Delete user in userList
		del userList[inputIDNumber]
		# Save userList
		fileStore(0)
		# Print that delete operation succeeded.
		print 'ID Number: %d deleted.' % inputIDNumber

	# If user choosed 'Change user state to invalid'
	else:
		# Change user state to invalid.
		userList[inputIDNumber][3] = '0'
		# Save userList
		fileStore(0)
		# Print that state change operation succeeded.
		print 'ID Number: %d state changed to invalid.' % inputIDNumber

	# Pause.
	os.system('pause')

# Function that prints main screen and handles initial operations.
def init():
	# Load files.
	fileLoad()

	# Repeat this block infinitely.
	while True:
		# Change window size.
		os.system('mode con: cols=100 lines=27')
		# Print main screen.
		print '''


       ____              _      __  __                                                   _   
      |  _ \            | |    |  \/  |                                                 | |  
      | |_) | ___   ___ | | __ | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
      |  _ < / _ \ / _ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
      | |_) | (_) | (_) |   <  | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
      |____/ \___/ \___/|_|\_\ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                                                          __/ |                              
                                                         |___/                               
                        _____           _                          __   ___  
                       / ____|         | |                        /_ | / _ \ 
                      | (___  _   _ ___| |_ ___ _ __ ___     __   _| || | | |
                       \___ \| | | / __| __/ _ \ '_ ` _ \    \ \ / / || | | |
                       ____) | |_| \__ \ ||  __/ | | | | |    \ V /| || |_| |
                      |_____/ \__, |___/\__\___|_| |_| |_|     \_/ |_(_)___/ 
                               __/ |                                         
                              |___/                                          


                                    Book Management System v1.0
                         Copyright (c) 2016 Jihun Kim. All rights reserved.
                                       !! READ ReadMe.txt !!

'''
		# Pause.
		os.system('pause > nul')

		# If the number of logined account is 0
		if currentAccount == 0:
			# Call guest menu
			guestMenu()

		# If the number of logined account is 1
		elif currentAccount == 1:
			# Call admin menu
			adminMenu()

		# If the number of logined account is neither 0 nor 1
		else:
			# Call user menu
			userMenu()

# Function that prints guest menu.
def guestMenu():
	# Repeat when current account is guest.
	while currentAccount == 0:
		# Change window size.
		os.system('mode con: cols=60 lines=30')
		# Print guest menu.
		print '\n\n Hi! You are a guest user.'
		print ' Login or Sign up, then you can use more functions.'
		print ' Choose the menu you want.\n\n'
		print ' ____ GUEST MENU ____\n'
		print ' [ 1 ] Print all books'
		print ' [ 2 ] Search the book'
		print ' [ 3 ] Login'
		print ' [ 4 ] Sign up'
		print ' ____________________\n'

		# Repeat until get valid input.
		while (True):
			# Get user input.
			selected_menu = raw_input('>> Menu number: ')
			# If user input is valid
			if selected_menu in ['1','2','3','4']:
				# Break this loop
				break
			# If not, print that the input is invalid.
			print 'Invalid Input. You have to input a number of the menu.\n'

		# If user selected 'Print all books' menu
		if selected_menu == '1':
			# Call bookPrint() function
			bookPrint()

		# If user selected 'Search the book' menu
		if selected_menu == '2':
			# Call bookSearch() function
			bookSearch()

		# If user selected 'Login' menu
		if selected_menu == '3':
			# Call login() function
			login()

		# If user selected 'Sign up' menu
		if selected_menu == '4':
			# Call signUp() function
			signUp()

# Function that prints admin menu.			
def adminMenu():
	# Repeat when current account is admin.
	while currentAccount == 1:
		# Change window size.
		os.system('mode con: cols=60 lines=30')
		# Print admin menu.
		print '\n\n Hello, Admin!'
		print ' Always be careful at managing books.'
		print ' Choose the menu you want.\n\n'
		print ' ____ ADMIN MENU ____\n'
		print ' 1 | Print all books'
		print ' 2 | Search the book'
		print ' 3 | Insert new book'
		print ' 4 | Delete existing book'
		print ' 5 | Permit account unlock request'
		print ' 6 | Delete existing user'
		print ' 7 | Logout'
		print ' 8 | Shutdown system'
		print ' ___________________\n'

		# Repeat until get valid input.
		while (True):
			# Get user input.
			selected_menu = raw_input('>> Menu number: ')
			# If user input is valid
			if selected_menu in ['1','2','3','4','5','6','7','8']:
				# Break this loop
				break
			# If not, print that the input is invalid.
			print 'Invalid Input. You have to input a number of the menu.\n'

		# If user selected 'Print all books' menu
		if selected_menu == '1':
			# Call bookPrint() function.
			bookPrint()

		if selected_menu == '2':
			# Call bookSearch() function.
			bookSearch()

		# If user selected 'Insert new book' menu
		if selected_menu == '3':
			# Call bookInsert() function.
			bookInsert()

		# If user selected 'Delete existing book' menu
		if selected_menu == '4':
			# Call bookDelete() function.
			bookDelete()

		# If user selected 'Permit account unlock request' menu
		if selected_menu == '5':
			# Call userPermit() function.
			userPermit()

		# If user selected 'Delete existing user' menu
		if selected_menu == '6':
			# Call userDelete() function.
			userDelete()

		# If user selected 'Logout' menu
		if selected_menu == '7':
			# Call logout() function.
			logout()

		# If user selected 'Shutdown system' menu
		if selected_menu == '8':
			# Call exitProgram() function.
			exitProgram()
		
# Function that prints user menu.
def userMenu():
	# Repeat when current account is user.
	while currentAccount not in range(1):
		# Change window size.
		os.system('mode con: cols=60 lines=30')
		# Print hello message.
		print '\n\n Hello, %s.'%userList[currentAccount][2]
		print ' Have you heard this famous saying?\n'
		# Make a random number.
		ran = random.randint(1,7)
		if ran == 1: print ' "Books are food for the mind."'
		if ran == 2: print ' "How many a man has dated a new era in his life\n  from the reading of a book."'
		if ran == 3: print ' "Reading is to the mind what exercise is to the body."'
		if ran == 4: print ' "You can cover a great deal of country in books."'
		if ran == 5: print ' "The love of learning, the sequestered nooks,\n  And all the sweet serenity of books."'
		if ran == 6: print ' "A truly great book should be read in youth,\n  again in maturity and once more in old age."'
		if ran == 7: print ' "I\'ve never known any trouble that an hour\'s\n  reading didn\'t assuage."'
		print '\n Have a good day with reading books!'
		print ' Choose the menu you want.\n\n'
		# Print user menu.
		print ' ___ USER MENU ___\n'
		print ' 1 | Print all books'
		print ' 2 | Search the book'
		print '   |  & Borrow it'
		print ' 3 | Return the book'
		print ' 4 | Logout'
		print ' _________________\n'

		# Repeat until get valid input.
		while (True):
			# Get user input.
			selected_menu = raw_input('>> ')
			# If user input is valid
			if selected_menu in ['1','2','3','4']:
				# Break this loop
				break
			# If not, print that the input is invalid.
			print 'Invalid Input. You have to input a number of the menu.\n'

		# If user selected 'Print all books' menu
		if selected_menu == '1':
			# Call bookPrint() function.
			bookPrint()

		# If user selected 'Search the book' menu
		if selected_menu == '2':
			# Call bookSearch() function.
			bookSearch()

		# If user selected 'Return the book' menu
		if selected_menu == '3':
			# Call bookReturn() function.
			bookReturn()

		# If user selected 'Logout' menu
		if selected_menu == '4':
			# Call logout() function.
			logout()

# Call init() function 
init()