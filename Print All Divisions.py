import math
# math.sq
def alldivision(n):
    list=[]
    sqrt=math.sqrt(n)
    dup=math.ceil(sqrt)
    for i in range(n,dup):
        if(n%i==0):
            l1=list.append(i)
            if(n/i != i):
                l1=list.append(n/i)
                print(l1)
    print()
n=int(input("Enter the number"))
print(alldivision(n))