import timeit as time
import platform as plfrm
import psutil as sysinfo
import random as ran
import matplotlib.pyplot as plt
# System Information
def get_cpu():
    return f"CPU: {plfrm.processor()}"
def get_ram():
    ram = sysinfo.virtual_memory()
    return f"Total RAM: {ram.total} bytes"
def get_stor():
    parts = sysinfo.disk_partitions()
    stor = []
    for part in parts:
        part_info = sysinfo.disk_usage(part.mountpoint)
        stor.append(f"{part.device} - Total: {part_info.total} bytes, Free: {part_info.free} bytes")
    return stor
def get_sys():
    return f"System: {plfrm.system()} {plfrm.version()}"

# Insertion Sort
def insertion_sort(array):
    for ind in range(1, len(array)):
        ele = array[ind]
        index = ind - 1
        while index >= 0:
            if array[index] > ele:
                array[index + 1] = array[index]
                index -= 1
            else:
                break
        array[index + 1] = ele

# Selection Sort
def sel_sort(array):
     for start_ind in range(len(array)):
        smallest_element=array[start_ind]
        ele_ind=start_ind
        for i in range(start_ind+1,len(array)):
            if(array[i]<smallest_element):
                smallest_element=array[i]
                ele_ind=i
        # if(smallest_element!=array[start_ind]):
        array[start_ind],array[ele_ind]=array[ele_ind],array[start_ind]
        # else:break

# Bubble Sort
def bubble_sort(array):
    for _ in range(len(array)):
        for ele in range(len(array)-1):
            if(array[ele]>array[ele+1]):
                array[ele],array[ele+1]=array[ele+1],array[ele]

# Function to generate a random array of a given size
def generate_random(size):
    return [ran.randint(1, 1000) for _ in range(size)]

# Function to benchmark sorting algorithms
def benchmark(sort_func, array):
    setup_code = f"from __main__ import {sort_func}, generate_random; arr = generate_random({len(array)})"
    stmt = f"{sort_func}(arr)"

    # Measure the execution time
    exe_time = time.timeit(stmt, setup=setup_code, number=10)

    return exe_time

# Benchmark parameters
sizes = [5, 10, 20, 50, 100, 200, 500, 1000,2000]  # Adjust as needed

# Results dictionary to store benchmark results
results = {'Insertion Sort': [], 'Selection Sort': [], 'Bubble Sort': []}

# Run benchmarks for each sorting algorithm and array size
for size in sizes:
    array = generate_random(size)

    # Insertion Sort
    ins_time = benchmark('insertion_sort', array)
    results['Insertion Sort'].append(ins_time)

    # Selection Sort
    sel_time = benchmark('sel_sort', array)
    results['Selection Sort'].append(sel_time)

    # Bubble Sort
    bub_time = benchmark('bubble_sort', array)
    results['Bubble Sort'].append(bub_time)

# System Information
print("System Information:")
print(get_cpu())    #output: CPU: Windows 10.0.22621
print(get_ram())    #output: Total RAM: 16805036032 bytes
print(get_sys())    #output: System: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

# Storage Information

print("Storage Information")
print('\n'.join(get_stor()))

"""output:C: - Total: 368129863680 bytes, Free: 243057664000 bytes
D: - Total: 318787022848 bytes, Free: 257257058304 bytes
E: - Total: 335544315904 bytes, Free: 316200505344 bytes
G: - Total: 16106127360 bytes, Free: 661610496 bytes"""

# Plotting the results
plt.plot(sizes, results['Insertion Sort'], label='Insertion Sort', color='green')
plt.plot(sizes, results['Selection Sort'], label='Selection Sort', color='blue')
plt.plot(sizes, results['Bubble Sort'], label='Bubble Sort', color='orange')

plt.xlabel('Array Size')
plt.ylabel('Execution Time (sec)')
plt.title('Benchmark Sorting Algorithm')
plt.legend()
plt.show()
