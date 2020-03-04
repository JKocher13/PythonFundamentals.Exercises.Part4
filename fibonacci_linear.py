n=int(input("What is your number?   "))

def fibonacci_lin(n):
	fibonacci_numbers = [0,1]
	for i in range(2,n):
		fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
	return (fibonacci_numbers[n-1])


print (fibonacci_lin(n+1))
  
