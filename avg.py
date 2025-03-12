def average(n):

    a=[]
    for i in range(0,n):
        ele=int(input("enter value"))
        a.append(ele)
    avg=sum(a)/n
    print(avg)
n=int(input("how many numbers you want to find the average"))  
average(n)

    