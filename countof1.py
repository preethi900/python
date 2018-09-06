#count the 1's

n = input("enter a number:")

result = str(bin(n)[2:])

final = result.count("1") 

print final
