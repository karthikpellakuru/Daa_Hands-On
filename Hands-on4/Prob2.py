#Question: Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

def dup(arr):
    if not arr:
        return []

    n = len(arr)
    temp = 0
    for i in range(1, n):
        if arr[i] != arr[temp]:
            temp += 1
            arr[temp] = arr[i]
    return arr[:temp + 1]

arr = input("Enter a sorted array : ")
input_array = list(map(int, arr.split()))
output_array = dup(input_array)

print("Original array: ",input_array)
print("Array after removing the duplicate elements: ",output_array)

---OUTPUT---
Enter a sorted array : 2 2 2
Original array:  [2, 2, 2]
Array after removing the duplicate elements:  [2]

Process finished with exit code 0
