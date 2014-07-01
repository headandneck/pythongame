import time, sys

def dead(why):
	print why
	exit(0)

def start():
	print "You finally reach the office."
	print "There is a computer and a desk."
	print "Which do you check?"

	prompt = raw_input("Computer or desk? ")

	if "computer" in prompt:
		computer()
	elif "desk in prompt":
		desk()
	else:
		dead("error!")

def computer():
	print "The screen lights up.\n\n"
	print "Welcome. Please enter your password\n"

	tries = 1

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

	firstscreen()	
	

def firstscreen():
	print "Login successful..."
	print "\nWelcome to the mainframe."		
	print "\nGathering list of files.\n"

	print """ 
	accounts.txt ...... 10/08/2014
	july_13_14.txt .... 11/05/2014
	explode.exe ....... 22/02/2013
	"""


computer()
