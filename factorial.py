#factorial program

def factorial(userinput):
	if userinput == 0:
		return 1
	else:
		return userinput * factorial(userinput -1)


inputfromuser = int(raw_input("enter a number:"))

answer = factorial(inputfromuser)
print answer
