#Check the adjacent bits

i = int(input("Enter a integer:"))

binary = str(int('{:032b}'.format(i)))

result = all(dup not in binary for dup in ("11","00"))


print result

