# Experiment 14: Second-Degree Polynomial Fitting

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define second-degree polynomial
def polynomial(x, a, b, c):
    return a * x**2 + b * x + c


# Take input
n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    print("\nData Point", i + 1)

    x_value = float(input("Enter x: "))
    y_value = float(input("Enter y: "))

    x.append(x_value)
    y.append(y_value)


x = np.array(x)
y = np.array(y)

# Fit polynomial
coefficients, covariance = curve_fit(
    polynomial, x, y
)

a, b, c = coefficients

print("\nPolynomial Coefficients:")
print("a =", a)
print("b =", b)
print("c =", c)

print("\nFitted Polynomial:")
print(f"y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")


# Generate fitted curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = polynomial(x_curve, a, b, c)

# Plot original points and fitted curve
plt.scatter(x, y, label="Original Data")
plt.plot(x_curve, y_curve, label="Fitted Curve")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Second-Degree Polynomial Fitting")

plt.legend()
plt.grid()
plt.show()