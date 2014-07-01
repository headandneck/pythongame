# A work in progress
# A text adventure game to get to grips with bits of Python
# If I had the commitment I'd make this the scale of Myst
# but with more cyber-punk overtones.
# If anyone ever finds this, please make the text green
# so it looks like an 80s terminal.

import time, sys

def dead(why):
	"""Exits the program and returns a reason why"""
	print why
	exit(0)

def start():
	print "You finally reach the office."
	print "There is a computer and a desk."
	print "Which do you check?"

	next = raw_input("Computer or desk? ")

	if "computer" in next:
		computer()
	elif "desk" in next:
		desk()
	else:
		dead("error!") # this will be updated to be more meaningful

def computer():
	print "The screen lights up.\n\n"
	print "Welcome. Please enter your password\n"

	tries = 1

	# Kind of proud of this. Keeps a track of unsuccessful logins,
	# then boots you out of the game if you get it wrong too many times.
	while tries <= 5:

		triesremaining = 5 - tries

		next = raw_input("|")

		if next == "abcd":
			break
		else:
			print "Incorrect password. You have %d tries remaining" % triesremaining
			tries += 1

		if tries == 6:
			dead("\nYou failed to enter the correct password. The system is locked.")
		else:
			pass
	# The 'break' in the while loop above leads to here.
	# There's probably a better way to do it.		
	firstscreen()	

def firstscreen():
	print "Login successful..."
	print "\nWelcome to the mainframe."		
	print "\nGathering list of files.\n"

	print """ 
	1. accounts.txt ...... 10/08/2014
	2. july_13_14.txt .... 11/05/2014
	3. explode.exe ....... 22/02/2013
	"""

	print "\nSelect file number: "

	while True: 

		next = raw_input("|")

		if next == "1":
			accounts()
		elif next == "2":
			july_13()
		elif next == "3":
			explode()
		else:
			print "Please enter a valid file number."

def accounts(): # temporary
	print "Acc"

def july_13(): # temporary
	print "July"

def explode(): # temporary
	print "Expl"

# Game begins - should be 'start() but for testing I change this to suit'
computer()
