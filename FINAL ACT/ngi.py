import math
from scipy.stats import norm

def margin_of_error_calculator():
    print("📦 Margin of Error Calculator (with known population σ)")

    # Inputs
    sigma = float(input("Enter the population standard deviation (σ): "))
    n = int(input("Enter the sample size (n): "))
    confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))

    # Step 1: Compute z-critical value
    alpha = 1 - confidence_level
    z_critical = norm.ppf(1 - alpha / 2)

    # Step 2: Compute standard error (SE)
    se = sigma / math.sqrt(n)

    # Step 3: Compute margin of error (ME)
    me = z_critical * se

    # Output
    print(f"\n📊 Z-critical value: {z_critical:.4f}")
    print(f"📉 Standard Error: {se:.4f}")
    print(f"✅ Margin of Error: {me:.4f}")

# Run the calculator
margin_of_error_calculator()
