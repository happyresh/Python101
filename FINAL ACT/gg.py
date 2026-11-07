import math
from scipy.stats import norm

def sampling_distribution_probability():
    print("📦 Sampling Distribution Probability Calculator")

    # Input
    mu = float(input("Enter the population mean (μ): "))
    sigma = float(input("Enter the population standard deviation (σ): "))
    n = int(input("Enter the sample size (n): "))
    x_bar = float(input("Enter the sample mean to test (x̄): "))
    tail = input("Find P(X̄ ≥ x̄) or P(X̄ ≤ x̄)? Type '>=' or '<=': ")

    # Standard error
    se = sigma / math.sqrt(n)

    # Z-score
    z = (x_bar - mu) / se

    # Compute probability
    if tail == ">=":
        p = 1 - norm.cdf(z)
    elif tail == "<=":
        p = norm.cdf(z)
    else:
        print("Invalid input for tail direction.")
        return

    # Output
    print(f"\n📊 Z-score: {z:.4f}")
    print(f"✅ Probability: {p:.4f} ({p*100:.2f}%)")

# Run the calculator
sampling_distribution_probability()
