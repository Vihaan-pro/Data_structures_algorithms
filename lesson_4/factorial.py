def factorial_n(n):
    if n==0:
        return 1 # factorial of 0 is 1 
    else:
        return n*factorial_n(n-1)
    

print(factorial_n(4))