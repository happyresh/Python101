import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Given data
mean = 48  # Average water intake in liters
variance = 8.4681  # Variance in liters
std_dev = np.sqrt(variance)  # Standard deviation

# Values for probability calculation
lower_bound = 45.2  # liters
upper_bound = 49.4  # liters

print("Water Intake Distribution Analysis")
print("=" * 40)
print(f"Mean (μ): {mean} liters")
print(f"Variance (σ²): {variance} liters²")
print(f"Standard Deviation (σ): {std_dev:.4f} liters")
print()

# Calculate the probability P(45.2 < X < 49.4)
# Using the cumulative distribution function (CDF)
prob_upper = stats.norm.cdf(upper_bound, mean, std_dev)
prob_lower = stats.norm.cdf(lower_bound, mean, std_dev)
probability = prob_upper - prob_lower

print(f"Probability Calculation:")
print(f"P(X < {upper_bound}) = {prob_upper:.6f}")
print(f"P(X < {lower_bound}) = {prob_lower:.6f}")
print(f"P({lower_bound} < X < {upper_bound}) = {probability:.6f}")
print(f"P({lower_bound} < X < {upper_bound}) = {probability:.2%}")

# Calculate Z-scores for additional insight
z_lower = (lower_bound - mean) / std_dev
z_upper = (upper_bound - mean) / std_dev

print()
print(f"Z-score Analysis:")
print(f"Z-score for {lower_bound} liters: {z_lower:.4f}")
print(f"Z-score for {upper_bound} liters: {z_upper:.4f}")

# Create a visualization
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y = stats.norm.pdf(x, mean, std_dev)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='Normal Distribution')

# Fill the area between 45.2 and 49.4
x_fill = np.linspace(lower_bound, upper_bound, 100)
y_fill = stats.norm.pdf(x_fill, mean, std_dev)
plt.fill_between(x_fill, y_fill, alpha=0.3, color='red', 
                 label=f'P({lower_bound} < X < {upper_bound}) = {probability:.4f}')

plt.axvline(mean, color='black', linestyle='--', alpha=0.7, label=f'Mean = {mean}')
plt.axvline(lower_bound, color='red', linestyle='--', alpha=0.7)
plt.axvline(upper_bound, color='red', linestyle='--', alpha=0.7)

plt.xlabel('Water Intake (liters)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of Filipino Water Intake')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print()
print("Summary:")
print(f"The probability that a randomly selected Filipino has")
print(f"a minimum water intake between {lower_bound} and {upper_bound} liters is {probability:.4f} or {probability:.2%}")