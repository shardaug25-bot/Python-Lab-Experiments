from scipy.optimize import minimize

print("This experiment minimizes a quadratic function f(x) = a*x^2 + b*x + c, where a must be positive.")
a = float(input("Enter a (> 0): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
start = float(input("Enter initial guess for x: "))
if a <= 0:
    raise ValueError("For a finite minimum, a must be greater than zero.")

def objective(values):
    x = values[0]
    return a*x*x + b*x + c

result = minimize(objective, [start])
print("Minimum x:", result.x[0])
print("Minimum function value:", result.fun)