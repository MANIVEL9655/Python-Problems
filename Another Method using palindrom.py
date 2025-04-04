from numpy.ma.core import count


def pal(n):
    revnum=0
    dup = n
    while(n>0):
        last_digit=n%10
        revnum=revnum*10+last_digit
        n=n//10
    if dup==revnum:
        print("The Number is Palindrome")
    else:
        print("Not a palindrome")
    return revnum
n=int(input("enter a number"))
print(pal(n))