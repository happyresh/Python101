from sympy import symbols, Rational, simplify

# Declare symbol for population mean
mu = symbols('mu')

# Coefficients as exact fractions
a = Rational(1, 7)
b = Rational(4, 15)
x_mu_coeff = Rational(4, 31)
y_mu_coeff = Rational(29, 65)

# Expected values
E_X = x_mu_coeff * mu
E_Y = y_mu_coeff * mu

# Estimator expectation
E_estimator = simplify(a * E_X + b * E_Y)

# Bias
bias = simplify(E_estimator - mu)

# Output
print(f"📌 E[X] = {x_mu_coeff}μ")
print(f"📌 E[Y] = {y_mu_coeff}μ")
print(f"📌 E[Estimator] = {E_estimator}")
print(f"📌 Bias = {bias}")
