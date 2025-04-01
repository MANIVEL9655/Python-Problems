def M_pattern(n):
    for row in range(n):
        for col in range(n):
            if ((col==0 or
            col==n-1) or
            row + col == (n - 1 and row < n / 2) or
            row == col and row<n/2 ):
                print("*", end=" ")
            else:
                print(" ")
n=int(input("Enter a Number"))
M_pattern(n)