#Length of last word

inputstring = raw_input("Enter a string:")

inputstring = inputstring.strip(" ")
split = inputstring.split(" ")

if len(split)==0:
	print 0
elif len(split)==1:
	print len(split[0])
else:
	print len(split[-1])


