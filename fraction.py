from math import comb
from fractions import Fraction

def hypergeometric_fraction():
    print("🎯 Hypergeometric Probability Calculator (Exact Fraction Output)\n")

    try:
        N = int(input("Enter total population size (N): "))
        K = int(input("Enter number of 'successes' in population (K): "))
        n = int(input("Enter number of draws (n): "))
        x = int(input("Enter number of observed 'successes' (x): "))

        # Compute numerator and denominator
        numerator = comb(K, x) * comb(N - K, n - x)
        denominator = comb(N, n)

        # Express probability as a simplified fraction
        probability = Fraction(numerator, denominator)

        print(f"\n✅ Probability P(X = {x}): {numerator}/{denominator}")
        print(f"➕ Simplified: {probability} (≈ {float(probability):.4f})")

    except Exception as e:
        print("⚠️ Error:", e)
        print("Please make sure all inputs are valid integers and that 0 ≤ x ≤ n.")

# Run the function
hypergeometric_fraction()
