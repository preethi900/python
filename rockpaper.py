#Rock ,paper scissors game

from random import randint

player = raw_input("select any one: (s) for scissors,(r) for rock,(p) for paper:")

#print(player, 'vs')

choose = randint(1,3)

#print(choose)

if choose == 1:
	comp = 's'
elif choose == 2:
	comp = 'r'
else:
	comp = 'p'
print(player , 'vs' ,comp)

if player == comp:
	print("draw")
elif comp == 'r' and player == 'p':
	print("player wins")
elif comp == 'p' and player == 'r':
	print("comp wins")
elif comp == 'p' and player == 's':
	print("player wins")
elif comp == 's' and player == 'p':
	print("comp wins")
elif comp == 'r' and player == 's':
	print("comp wins")
else:
	print("player wins") 


