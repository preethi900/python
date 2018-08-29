#Reverse to binary for an integer


i = int(input("Enter an integer:"))

binary = int('{:032b}'.format(i)[::-1], 2)


print binary
