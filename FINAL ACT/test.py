import math
from scipy.stats import norm

def probability_sample_mean_at_least(mu, sigma, n, x_bar_threshold):
    """
    Calculates the probability that the sample mean is at least a given value.
    
    Parameters:
    - mu: population mean
    - sigma: population standard deviation
    - n: sample size
    - x_bar_threshold: the threshold sample mean
    
    Returns:
    - probability: P(sample mean >= x_bar_threshold)
    - z_score: calculated Z value
    """

    # Calculate standard error
    standard_error = sigma / math.sqrt(n)

    # Compute Z-score
    z = (x_bar_threshold - mu) / standard_error

    # Get probability P(X̄ ≥ x_bar_threshold) = 1 - P(Z ≤ z)
    probability = 1 - norm.cdf(z)

    return probability, z

# 🧑‍💻 Input Section
print("📊 Z-Probability Calculator for Sample Mean (Full Precision)\n")

try:
    mu = float(input("Enter the population mean (μ): "))
    sigma = float(input("Enter the population standard deviation (σ): "))
    n = int(input("Enter the sample size (n): "))
    x_bar_threshold = float(input("Enter the threshold sample mean (x̄): "))

    # Calculate
    prob, z_score = probability_sample_mean_at_least(mu, sigma, n, x_bar_threshold)

    # Output
    print("\n📈 Results (No Rounding):")
    print(f"Z-score: {z_score}")
    print(f"Probability that the sample mean is at least PHP {x_bar_threshold:,.2f}: {prob * 100}%")

except ValueError:
    print("⚠️ Please enter valid numeric values.")
