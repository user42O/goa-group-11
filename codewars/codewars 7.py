def find_smallest_integer(arr):
    smallest = arr[0] 
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr1 = [34, 15, 88, 2]
print(find_smallest_integer(arr1))  

arr2 = [34, -345, -1, 100]
print(find_smallest_integer(arr2))  
