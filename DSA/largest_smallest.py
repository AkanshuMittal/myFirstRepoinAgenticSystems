def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < minimum:
           minimum = arr[i]
        elif arr[i] > maximum:
            maximum = arr[i]
    
    return minimum, maximum

arr = [3,5,2,7,10,45]

min_val, max_val = find_min_max(arr)

print(f"Smallest value {min_val} Largest Value {max_val}")


