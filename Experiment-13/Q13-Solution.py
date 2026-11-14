# Experiment 13: Numerical Differentiation and Integration

import numpy as np
from scipy.optimize import approx_fprime
from scipy.integrate import quad

# Take coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Define function
def f(x):
    return a * x**2 + b * x + c


# Numerical differentiation
x0 = float(input("\nEnter point for differentiation: "))

derivative = approx_fprime(
    np.array([x0]),
    lambda x: f(x[0]),
    epsilon=1e-6
)

print("\nNumerical Differentiation:")
print("Derivative at", x0, "=", derivative[0])


# Numerical integration
lower = float(input("\nEnter lower limit: "))
upper = float(input("Enter upper limit: "))

result, error = quad(f, lower, upper)

print("\nNumerical Integration:")
print("Integration result:", result)
print("Estimated error:", error)