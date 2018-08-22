#Reverse using function

def reverse_string(inputstring):
	index = len(inputstring)
	newstring = ''
	while index:
		index -= 1
		newstring += inputstring[index]
	return newstring

output = reverse_string("hello")
print output
