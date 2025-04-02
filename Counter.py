def M_pattern(n):
    for i in range(n):
        for j in range(n):
          
            if j == 0 or j==n-1 or (i==j and j<=n//2) or (i+j == n-1 and j>=n//2):
                print("*", end=" ")
            else:
                print(" ")
n=int(input("Enter a Number"))

M_pattern(n)