from scipy.linalg import sqrtm


def amstronf(n):
    sum=0
    dup=n
    while(n>0):
        last_digit=n%10
        sum=sum+(last_digit*last_digit*last_digit)
        n = n // 10
    if(sum==dup):
        print("The number is amstrong")
    else:
        print("Not an amstrong")
n=int(input("Enter the Number"))
amstronf(n)
