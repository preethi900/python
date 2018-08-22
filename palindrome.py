#check if its palindrome or not

string = raw_input("enter any string:")


if (string == string[::-1]):

	print ("the string is a palindrome")
else:
	print ("the string is not a palindrome")

