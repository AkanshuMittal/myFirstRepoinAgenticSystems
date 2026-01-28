def Secondlargest(arr):
    n = len(arr)
    if n < 2: 
        return [-1]
    
    largest = arr[0]
    slargest = float('-inf')
    smallest = arr[0]
    ssmallest = float('inf')
    
    for i in range(1, n):
        if arr[i] > largest:
          slargest = largest 
          largest = arr[i]
        
        elif arr[i] < largest and arr[i] > slargest:
            slargest = arr[i]
            
    for i in range(1, n):
        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]
            
        elif arr[i] < smallest and arr[i] != smallest:
            ssmallest = arr[i]
            
    return [slargest, ssmallest]


arr = [3,6,1,9,10]
slargest, ssmallest = Secondlargest(arr)

print(f"Second Largest {slargest} and Second Smallest {ssmallest}")
         
    
        
    