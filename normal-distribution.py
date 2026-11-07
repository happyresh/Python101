import math
from scipy.stats import norm

def normal_distribution_probability():
    print("Normal Distribution Probability Calculator")
    
    # User input
    mu = float(input("Enter the mean (μ): "))
    sigma = float(input("Enter the standard deviation (σ): "))
    
    print("\nEnter the bounds (use -inf or inf if needed):")
    lower_bound = input("Lower bound: ")
    upper_bound = input("Upper bound: ")

    # Convert bounds
    if lower_bound.lower() == "-inf":
        lower_bound = -math.inf
    else:
        lower_bound = float(lower_bound)

    if upper_bound.lower() == "inf":
        upper_bound = math.inf
    else:
        upper_bound = float(upper_bound)

    # Calculate Z-scores
    z_lower = (lower_bound - mu) / sigma if lower_bound != -math.inf else -math.inf
    z_upper = (upper_bound - mu) / sigma if upper_bound != math.inf else math.inf

    # Compute probability using CDF
    probability = norm.cdf(z_upper) - norm.cdf(z_lower)

    print("\n--- RESULTS ---")
    print(f"Z-score for lower bound: {z_lower:.4f}")
    print(f"Z-score for upper bound: {z_upper:.4f}")
    print(f"Probability that X is between {lower_bound} and {upper_bound}: {probability:.4f}")

# Run the function
normal_distribution_probability()
