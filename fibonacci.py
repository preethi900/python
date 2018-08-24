#Print the fibonacci series


inputnumber = int(raw_input("Enter the number:"))

num1 = 0
num2 = 1
count = 0

if (inputnumber == 0):
	print "0"
elif (inputnumber == 1):
	print "1"
else:

	while(count < inputnumber):
		fibonacci = num1 + num2
		print fibonacci
		num1 = num2
		num2 = fibonacci
 		count += 1 

