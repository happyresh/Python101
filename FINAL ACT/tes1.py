import math
from scipy.stats import norm

def confidence_interval_difference_proportions(x1, n1, x2, n2, confidence=0.95):
    # Step 1: Compute sample proportions
    p1 = x1 / n1
    p2 = x2 / n2

    # Step 2: Compute standard error
    se = math.sqrt((p1 * (1 - p1)) / n1 + (p2 * (1 - p2)) / n2)

    # Step 3: Find z-value
    z = norm.ppf(1 - (1 - confidence) / 2)

    # Step 4: Compute margin of error
    me = z * se

    # Step 5: Compute confidence interval
    diff = p1 - p2
    lower = diff - me
    upper = diff + me

    return (lower, upper), diff, me

# 🧑‍💻 Input Section
print("📊 Confidence Interval for Difference Between Two Proportions\n")

try:
    x1 = int(input("Enter number of middle-aged in group 1 (e.g., students): "))
    n1 = int(input("Enter total number in group 1: "))
    x2 = int(input("Enter number of middle-aged in group 2 (e.g., professionals): "))
    n2 = int(input("Enter total number in group 2: "))
    confidence = float(input("Enter confidence level as decimal (e.g., 0.95 for 95%): "))

    ci, diff, me = confidence_interval_difference_proportions(x1, n1, x2, n2, confidence)

    # Output
    print("\n📈 Results (No Rounding):")
    print(f"Difference in proportions (p1 - p2): {diff}")
    print(f"Margin of Error: {me}")
    print(f"{int(confidence * 100)}% Confidence Interval: ({ci[0]}, {ci[1]})")

except ValueError:
    print("⚠️ Please enter valid numeric values.")
