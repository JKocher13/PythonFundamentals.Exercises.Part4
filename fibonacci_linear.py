n=int(input("What is your number?   "))

def fibonacci_lin(x):
	fibonacci_numbers = [0,1]
	for i in range(2,x+1):
		fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
	return (fibonacci_numbers[x])


print (fibonacci_lin(n))
  
