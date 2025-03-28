n=5
for i in range(n):
    for j in range(n):
        if j<n-i-1:
            print(end="  ")
    for j in range(n):
        if j<2*i+1:
            print("*")
    for j in range(n):
        if j<n-i-1:
            print(end=" ")
    print()