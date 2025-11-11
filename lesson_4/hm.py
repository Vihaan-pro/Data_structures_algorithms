def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test the function
for i in range(10):  # Print the first 10 Fibonacci numbers
    print(f"fibonacci({i}) = {fibonacci(i)}")

#print(fibonacci(10))