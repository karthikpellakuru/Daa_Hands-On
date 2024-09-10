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

# Fit a polynomial curve to the data
fit_coefficients = np.polyfit(n_values, execution_times, 2)
fitted_curve = np.polyval(fit_coefficients, n_values)

# Upper bound (Big-O): cubic polynomial
upper_bound_coefficients = np.polyfit(n_values, execution_times, 3)
upper_bound_curve = np.polyval(upper_bound_coefficients, n_values)
upper_bound_expression = np.poly1d(upper_bound_coefficients)

# Lower bound (Big-Omega): linear polynomial
lower_bound_coefficients = np.polyfit(n_values, execution_times, 1)
lower_bound_curve = np.polyval(lower_bound_coefficients, n_values)
lower_bound_expression = np.poly1d(lower_bound_coefficients)

# Print expressions
print("Fitted Curve:", np.poly1d(fit_coefficients))
print("Upper Bound (Big-O):", upper_bound_expression)
print("Lower Bound (Big-Omega):", lower_bound_expression)

# Plotting
plt.figure()
plt.plot(n_values, execution_times, 'bo', label='Data Points')
plt.plot(n_values, fitted_curve, 'r-', linewidth=2, label='Fitted Curve')
plt.plot(n_values, upper_bound_curve, 'g--', linewidth=2, label='Upper Bound')
plt.plot(n_values, lower_bound_curve, 'm--', linewidth=2, label='Lower Bound')
plt.legend()
plt.show()


OUTPUT:
Fitted Curve:            2
2.458e-08 x - 2.323e-07 x - 1.335e-06
Upper Bound (Big-O):           3             2
2.12e-10 x - 7.537e-09 x + 1.072e-06 x - 1.258e-05
Lower Bound (Big-Omega):  
2.251e-06 x - 4.355e-05

Process finished with exit code 0
