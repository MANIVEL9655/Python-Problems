def function(n):

    for i in range(1,n):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
n=int(input("Enter the number"))
function(n)