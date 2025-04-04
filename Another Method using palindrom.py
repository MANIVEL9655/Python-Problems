from numpy.ma.core import count


def pal(n):
    revnum=0
    count = 0
    while(n>0):
        last_digit=n%10
        revnum=revnum*10+last_digit
        n=n//10
        count=count+1
        print("The count of a number is",count)
        # if revnum == n:
        #     print("The Number is Palindrome")
        # else:
        #     print("Not a palindrome")
    return revnum
n=int(input("enter a number"))
print(pal(n))