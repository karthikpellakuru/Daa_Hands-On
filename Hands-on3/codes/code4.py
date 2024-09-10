import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x += 1
    return x

n_values = np.arange(1, 101)
execution_times = np.zeros_like(n_values, dtype=float)

for idx, n in enumerate(n_values):
    start_time = time.time()
    f(n)
    execution_times[idx] = time.time() - start_time

plt.plot(n_values, execution_times, 'bo', label='Data Points')
fit_coefficients = np.polyfit(n_values, execution_times, 2)
fitted_curve = np.polyval(fit_coefficients, n_values)
plt.plot(n_values, fitted_curve, 'r-', linewidth=2, label='Fitted Curve')

# Find the index where the execution time deviates from the fitted curve
deviation_index = np.argmax(execution_times > fitted_curve)

# Print the values
approx_n_0 = n_values[deviation_index]
execution_time_at_n_0 = execution_times[deviation_index]

print(f"Approximate n_0: {approx_n_0}")
print(f"Execution time at n_0: {execution_time_at_n_0} seconds")

# Plot a vertical line at the point of deviation
plt.axvline(x=approx_n_0, color='g', linestyle='--', label='Approx. n_0')

plt.legend()
plt.show()

OUTPUT:
Approximate n_0: 27
Execution time at n_0: 0.0009982585906982422 seconds

Process finished with exit code 0
