#Reverse words

def reversewords(s):

	return " ".join(s.strip().split()[::-1])


i = raw_input("enter a sentence:")

output = reversewords(i)

print output
