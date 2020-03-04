n = int(input("What is your number (between 0 and 30)?      "))
def fibonnaci(n):
	if n<=1:
		return(n)
	else:
		return(fibonnaci(n-1) + fibonnaci(n-2))
		
		

print(fibonnaci(n))
