n=int(input("enter the number"))
for i in range(n):
    for j in range(n-2):
        if (j==0 or j==n-3) or ((i==0 or i==4) and (j>0 and j<n-1)):
            print("*", end="")*
        else:
            print(end=" ")
    print()