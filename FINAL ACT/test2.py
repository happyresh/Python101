import math
from scipy.stats import norm

def one_proportion_z_test(x, n, p0, alpha=0.02):
    p_hat = x / n
    se = math.sqrt(p0 * (1 - p0) / n)
    z = (p_hat - p0) / se
    z_critical = norm.ppf(1 - alpha)

    # Decision logic
    if z > z_critical:
        decision = "Reject H0. There is sufficient evidence to support the claim."
    else:
        decision = "Do NOT reject H0. There is no sufficient evidence to support the claim."

    return {
        "p_hat": p_hat,
        "z_statistic": z,
        "z_critical": z_critical,
        "decision": decision
    }

# 🧑‍💻 Input your corrected values
x = 28
n = 47
p0 = 0.6614
alpha = 0.02

# Run the test
result = one_proportion_z_test(x, n, p0, alpha)

# Output the results
print("📊 One-Proportion Z-Test Result:")
for key, value in result.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
