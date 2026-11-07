import math
from scipy.stats import norm

def confidence_interval_proportion():
    print("📊 Confidence Interval Calculator for Population Proportion")

    # Input
    n = int(input("Enter sample size (n): "))
    x = int(input("Enter number of successes (x): "))
    confidence = float(input("Enter confidence level (e.g., 0.99 for 99%): "))

    # Step 1: Calculate p-hat
    p_hat = x / n

    # Step 2: Critical value (z-score)
    alpha = 1 - confidence
    z = norm.ppf(1 - alpha / 2)

    # Step 3: Standard error
    se = math.sqrt(p_hat * (1 - p_hat) / n)

    # Step 4: Margin of error
    me = z * se

    # Step 5: Confidence interval
    lower = p_hat - me
    upper = p_hat + me

    # Output
    print(f"\n✅ Proportion (p̂): {p_hat:.4f}")
    print(f"✅ Margin of Error: {me:.4f}")
    print(f"✅ Confidence Interval: ({lower:.4f}, {upper:.4f})")
    print(f"✅ In percent: ({lower*100:.2f}%, {upper*100:.2f}%)")

# Run the calculator
confidence_interval_proportion()
