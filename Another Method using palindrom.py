def pal(n):
    revnum=0
    while(n>0):
        last_digit=n%10
        revnum=(revnum*10)+last_digit
        n=n/10
    return revnum
n=int(input("enter a number"))
pal(n)