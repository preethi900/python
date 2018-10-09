#grouping team

from random import choice

players = ['sachin' , 'dravid' ,'harbhajan' ,'dhoni' , 'kohli']

print(players)

teama = []
teamb = []

while len(players) > 0:
	A = choice(players)
	teama.append(A)
	players.remove(A)
	if players == []:
		break
	B = choice(players)
	teamb.append(B)
        players.remove(B)

print ('TeamA:' ,teama)
print ('TeamB:' ,teamb)
