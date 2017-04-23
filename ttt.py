import numpy as np

turn = 5
field = [0]*9
game = ""

def set(pN):
	global turn
	global field
	global game
	if (pN < 9 and pN >= 0 and field[pN] == 0 ):
		game += str(pN + 1)
		field[pN] = turn		
		check()
		turn *= -1
		
	printGame()

def printGame():
	print(field[0:3])
	print(field[3:6])
	print(field[6:9])
	
def check():
	global game
	if( abs(np.sum(field[0:3])) == 15 or abs(np.sum(field[3:6])) == 15 or abs(np.sum(field[6:9])) == 15
		or abs(field[0]+field[3]+field[6]) == 15 or abs(field[1]+field[4]+field[7]) == 15 
		or abs(field[2]+field[5]+field[8]) == 15 or abs(field[0]+field[4]+field[8]) == 15 
		or abs(field[6]+field[4]+field[2]) == 15):
		game = game.ljust(9,'0')
		if(turn == 5):
			game += "x"
		else:
			game += "o"
		
		print("yay")
	else:
		print("doh")
	
def getStatus():
	return game
	
def test():


	set(0)
	set(5)
	set(4)
	set(6)
	set(8)


