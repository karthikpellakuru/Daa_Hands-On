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
plt.legend()
plt.show()
