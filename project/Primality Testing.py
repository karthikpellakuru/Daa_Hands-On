import time
import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Primality Testing Algorithms

# Trial Division
def trial_division(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Miller-Rabin Test (Probabilistic)
def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Write n - 1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

# Benchmarking Functions

# Benchmark with multiple runs for average time
def benchmark(func, *args, runs=5):
    times = []
    for _ in range(runs):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

# Simulated input sizes and corresponding benchmark times
input_sizes = [10, 101, 1009, 104729, 10**6 + 3]
trial_times = []
miller_times = []
sieve_times = []

for n in input_sizes:
    trial_times.append(benchmark(trial_division, n))
    miller_times.append(benchmark(miller_rabin, n, 5))
    sieve_times.append(benchmark(sieve_of_eratosthenes, n))

# Average times for comparison
average_times = [np.mean([trial, miller, sieve]) for trial, miller, sieve in zip(trial_times, miller_times, sieve_times)]

# Replace zeros in average_times to avoid division by zero
average_times = [max(time, 1e-9) for time in average_times]  # Use a very small value instead of zero

# Relative performance comparison
relative_performance = {
    "Trial Division": np.nan_to_num(np.array(trial_times) / np.array(average_times)),
    "Miller-Rabin": np.nan_to_num(np.array(miller_times) / np.array(average_times)),
    "Sieve of Eratosthenes": np.nan_to_num(np.array(sieve_times) / np.array(average_times)),
}

# Miller-Rabin Error Rates (simulated for demonstration)
error_rates = [0.1, 0.05, 0.02, 0.01, 0.005]

# Graphs

# Execution Time vs Input Size
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, trial_times, label="Trial Division", marker='o')
plt.plot(input_sizes, miller_times, label="Miller-Rabin", marker='o')
plt.plot(input_sizes, sieve_times, label="Sieve of Eratosthenes", marker='o', linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time vs Input Size")
plt.legend()
plt.grid(True)
plt.show()

# Execution Time Comparison for Larger Inputs
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, trial_times, label="Trial Division", marker='o', color='blue')
plt.plot(input_sizes, miller_times, label="Miller-Rabin", marker='o', color='orange')
plt.plot(input_sizes, average_times, label="Average Time", marker='x', linestyle='-.', color='purple')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time Comparison for Larger Inputs")
plt.legend()
plt.grid(True)
plt.show()

# Average Time Taken by Algorithms
plt.figure(figsize=(10, 6))
plt.bar(["Trial Division", "Miller-Rabin", "Sieve of Eratosthenes"], [np.mean(trial_times), np.mean(miller_times), np.mean(sieve_times)], color=['blue', 'orange', 'green'])
plt.ylabel("Average Time (s)")
plt.title("Average Time Taken by Algorithms")
plt.grid(axis='y')
plt.show()

# Relative Performance Comparison
plt.figure(figsize=(10, 6))
for algo, rel_perf in relative_performance.items():
    plt.plot(input_sizes, rel_perf, label=algo, marker='o')
plt.xscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Relative Performance")
plt.title("Relative Performance Comparison of Algorithms")
plt.legend()
plt.grid(True)
plt.show()

# Miller-Rabin Error Rate
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, error_rates, label="Error Rate", marker='o', color='red')
plt.xscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Error Rate")
plt.title("Miller-Rabin Error Rate vs Input Size")
plt.grid(True)
plt.legend()
plt.show()

# Testing the algorithms on specific inputs and printing the results
test_numbers = [7, 19, 97, 561, 1024]
print("Algorithm Results:")
for num in test_numbers:
    print(f"Number: {num}")
    print(f"  Trial Division: {trial_division(num)}")
    print(f"  Miller-Rabin: {miller_rabin(num, 5)}")
    if num <= 10**6:  # Sieve is only precomputed for smaller numbers
        sieve_result = sieve_of_eratosthenes(num)[num]
        print(f"  Sieve of Eratosthenes: {sieve_result}")
    print()

-----------OUTPUT------------------
Algorithm Results:
Number: 7
  Trial Division: True
  Miller-Rabin: True
  Sieve of Eratosthenes: True

Number: 19
  Trial Division: True
  Miller-Rabin: True
  Sieve of Eratosthenes: True

Number: 97
  Trial Division: True
  Miller-Rabin: True
  Sieve of Eratosthenes: True

Number: 561
  Trial Division: False
  Miller-Rabin: False
  Sieve of Eratosthenes: False

Number: 1024
  Trial Division: False
  Miller-Rabin: False
  Sieve of Eratosthenes: False


Process finished with exit code 0
