# def kthLargest(arr, k):
#     n =len(arr)
#     # Sort the given vector
#     arr.sort()

#     # Return k'th element in the sorted vector
#     return arr[n- k]



# arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
# k = 6

# print(kthLargest(arr, k))


import heapq 


def kthLargest(arr, k):
    
    # Create a max heap 
    pq = []

    # Iterate through the array elements
    for i in range(len(arr)):
        
        # Push the current element onto the max heap
        heapq.heappush(pq, arr[i])  

        # If the size of the max heap exceeds k,
        #remove the largest element
        if len(pq) > k:
            heapq.heappop(pq)

    return pq[0]

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 3

print(kthLargest(arr, k))
