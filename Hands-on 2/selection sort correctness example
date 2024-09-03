#selection sort correctness 

def sel_sort(arr):
    n = len(arr)
    for i in range(n):
        min_inx = i
        # find min element in array
        for j in range(i + 1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j
        # Swap min element with 1st element
        arr[i], arr[min_inx] = arr[min_inx], arr[i]

# Example 
arr = [94, 27, 62, 45, 11]
sel_sort(arr)
print("Sorted array:", arr)
