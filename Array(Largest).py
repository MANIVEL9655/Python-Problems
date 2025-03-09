def largest(arr):
    large=arr[0]
    for num in arr:
        if num > large:
            large=num
    return large
arr=[1,2,3,4,5,77,88,99,99]
print(largest(arr))