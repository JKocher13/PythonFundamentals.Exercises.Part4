from random import randrange

def highlow():
	x =int( input("Give me a number between 0 and 10: "))
	y = int(randrange(1,11))
	while(x != y):
		if x > y:
			print("Too High")
			x =int( input("Give me a number between 0 and 10: "))
		else:
			print("Too Low")
			x =int( input("Give me a number between 0 and 10: "))
	print("CORRECT!")
		
	print("Random Number was " + str(y))
highlow()
