def GCD(a,b):
    while(a>0&b>0):
        if(a>b):
            a=a%b
            print(a)
        else:
            b = b % a
            print(b)
        # print(a,b)
    # if(a==b):
    #     print(b)
    # else:
    #     print(a)
    # print()

a=int(input("Enter the number"))
b=int(input("Enter the number"))
GCD(a,b)