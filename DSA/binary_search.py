def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 

arr = [2, 4, 6, 8, 10]
target = 8

print(binary_search(arr, target))

# O(log n)

# O(1)