import random
import time
import matplotlib.pyplot as plt

def quick_sort(array):
    if len(array) <= 1:
        return array
    a = array[len(array) // 2]
    k = [x for x in array if x < a]
    s = [x for x in array if x == a]
    b = [x for x in array if x > a]
    return quick_sort(k) + s + quick_sort(b)

def benchmarks(inputs):
    et = []
    for i in inputs:
        start_time = time.time()
        quick_sort(i)
        end_time = time.time()
        et.append(end_time - start_time)
    return et


max_input_size = 200
array_size = list(range(1, max_input_size + 1))

best_case = [list(range(1, n + 1)) for n in array_size]
worst_case = [list(range(n, 0, -1)) for n in array_size]
average_case = [random.sample(range(1, n + 1), n) for n in array_size]

plt.plot(array_size,  benchmarks(best_case), label='Best Case')
plt.plot(array_size,  benchmarks(worst_case), label='Worst Case')
plt.plot(array_size, benchmarks(average_case), label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Benchmarks of Non-Random Pivot points')
plt.legend()
plt.show()
