#6. Implement merge sort, upload your code to github and show/test it on the array [5,2,4,7,1,3,2,6].

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while True:
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            else:
                break

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original Array:", arr)

merge_sort(arr)

print("Sorted Array:", arr)




'''Output:
Original Array: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted Array: [1, 2, 2, 3, 4, 5, 6, 7]
'''
