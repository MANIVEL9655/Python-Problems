def smallestnum(arr):
    if not arr:
        return "Empty array"
    smallest=arr[0]
    for num in arr:
        if num < smallest:
            smallest=num  
    return smallest
       

arr=[12,334,555,67,66,77,23,45,78,1,6]
print(smallestnum(arr))