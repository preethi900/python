#Reverse words in sentence

def reversed_sent(inputstring):

	return " ".join(word[::-1] for word in inputstring.split(" "))

string = raw_input("enter a sentence:")
output = reversed_sent(string)
print output
