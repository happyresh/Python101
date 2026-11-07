import math
from scipy.stats import norm

def two_population_means_ci():
    print("🏘️ Confidence Interval for μ₁ - μ₂ (Known σ₁ and σ₂)")

    # Inputs for Population 1
    mean1 = float(input("Enter the mean of the first population (X̄₁): "))
    sigma1 = float(input("Enter the population standard deviation σ₁: "))
    n1 = int(input("Enter the sample size for population 1 (n₁): "))

    # Inputs for Population 2
    mean2 = float(input("Enter the mean of the second population (X̄₂): "))
    sigma2 = float(input("Enter the population standard deviation σ₂: "))
    n2 = int(input("Enter the sample size for population 2 (n₂): "))

    # Confidence level
    confidence_level = float(input("Enter the confidence level (e.g., 0.90 for 90%): "))
    alpha = 1 - confidence_level
    z = norm.ppf(1 - alpha / 2)

    # Compute standard error
    se = math.sqrt((sigma1 ** 2) / n1 + (sigma2 ** 2) / n2)

    # Mean difference
    mean_diff = mean1 - mean2

    # Margin of Error
    me = z * se

    # Confidence interval
    lower = mean_diff - me
    upper = mean_diff + me

    # Output
    print(f"\n🔎 Z-critical value: {z:.4f}")
    print(f"📉 Standard Error: {se:.4f}")
    print(f"🧮 Margin of Error: {me:.4f}")
    print(f"\n✅ {int(confidence_level * 100)}% Confidence Interval: ({lower:,.2f}, {upper:,.2f})")

# Run the calculator
two_population_means_ci()
