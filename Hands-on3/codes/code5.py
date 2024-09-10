#Question: Will this increate how long it takes the algorithm to run (e.x. you are timing the function like in #2)?


import time
import numpy as np
import matplotlib.pyplot as plt

def original_f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x += 1
    return x

def modified_f(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x += 1
            y = i + j
    return x

n_values = np.arange(1, 10)
original_execution_times = np.zeros_like(n_values, dtype=float)
modified_execution_times = np.zeros_like(n_values, dtype=float)

for idx, n in enumerate(n_values):
    start_time = time.time()
    original_f(n)
    original_execution_times[idx] = time.time() - start_time

    start_time = time.time()
    modified_f(n)
    modified_execution_times[idx] = time.time() - start_time

    print(f'n = {n}: Original Time = {original_execution_times[idx]:.6f}s, Modified Time = {modified_execution_times[idx]:.6f}s')

plt.plot(n_values, original_execution_times, 'bo', label='Original Function')
plt.plot(n_values, modified_execution_times, 'go', label='Modified Function')
plt.legend()
plt.show()


OUTPUT:
n = 1: Original Time = 0.000000s, Modified Time = 0.000000s
n = 2: Original Time = 0.000000s, Modified Time = 0.000000s
n = 3: Original Time = 0.001001s, Modified Time = 0.000000s
n = 4: Original Time = 0.000000s, Modified Time = 0.000000s
n = 5: Original Time = 0.000000s, Modified Time = 0.000000s
n = 6: Original Time = 0.000000s, Modified Time = 0.000000s
n = 7: Original Time = 0.000000s, Modified Time = 0.000000s
n = 8: Original Time = 0.000000s, Modified Time = 0.000000s
n = 9: Original Time = 0.000000s, Modified Time = 0.000000s

Process finished with exit code 0
