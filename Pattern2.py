n=5
for i in range(n):
    for j in range(i+n):
        if j<=n-i-1:
            print(j,end=" ")
    print()