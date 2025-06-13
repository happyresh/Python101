from scipy.stats import hypergeom
from math import comb
from fractions import Fraction

# --- User Input ---
N = int(input("Enter total population size (N): "))
K = int(input("Enter number of success items (K): "))
n = int(input("Enter sample size (n): "))

print("\n--- Hypergeometric Distribution PMF & CDF ---")
print(f"Population (N): {N}, Successes (K): {K}, Sample size (n): {n}\n")

# Total possible values for X: max successes is min(K, n)
max_success = min(K, n)

# Compute total combinations (denominator of PMF)
total_comb = comb(N, n)

cdf_sum = 0
print(f"{'x':<5} {'P(X=x)':<20} {'CDF P(X≤x)':<20}")
print("-" * 45)

for x in range(0, max_success + 1):
    num = comb(K, x) * comb(N - K, n - x)
    frac = Fraction(num, total_comb).limit_denominator()
    prob = num / total_comb
    cdf_sum += prob
    cdf_frac = Fraction(cdf_sum).limit_denominator()

    print(f"{x:<5} {str(frac):<20} {str(cdf_frac):<20}")
