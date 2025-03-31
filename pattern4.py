def function(n):

    for i in range(1,n):
        for j in range(i):
            print(j,end=" ")
        print()
n=int(input("Enter the number"))
function(n)