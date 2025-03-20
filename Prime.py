def is_prime(n):
    if n//n==0 and n//1==0:
        print("The number is prime")
    else:
        print("The number is not a prime")
n=int(input("enter a number"))
is_prime(n)        
