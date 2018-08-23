# calculator program

def add(x,y):
	return x + y

def sub(x,y):
	return x - y

def mul(x,y):
	return x * y

def div(x,y):
	return x / y

print ("Welcome to the python calculator!")
print ("Enter any one of the choices below:")
print ("1.Addition")
print ("2.Subtraction")
print ("3.Multiply")
print ("4.Divide")


choice = raw_input("enter your choice (1/2/3/4):")

num1 = int(raw_input("Enter the first number:"))
num2 = int(raw_input("Enter the second number:"))


if choice == '1':
	 print(add(num1,num2))
elif choice == '2':
	print(sub(num1,num2))
elif choice == '3':
	print(mul(num1,num2))
elif choice == '4':
	print(div(num1,num2))
else:
	print("Invalid input")
