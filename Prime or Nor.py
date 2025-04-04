def prime(n):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count=count+1
            if(n/i !=i):
                count=count+1
    if count==2:
        print("True")
    else:
        print("False")
n=int(input("Enter the Number"))
print(prime(n))