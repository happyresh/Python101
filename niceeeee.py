from fractions import Fraction

def calculate_probability():
    # Favorable outcomes for each event
    favorable_A = 3   # Black Kings or 7♦
    favorable_B = 12  # 3, 4, 5 of any suit
    favorable_C = 6   # Jacks or black Aces
    favorable_D = 6   # 8s or red 9s

    # Denominators decrease due to no replacement
    total_1 = 52
    total_2 = 51
    total_3 = 50
    total_4 = 49

    # Multiply as fractions
    prob = Fraction(favorable_A, total_1) * \
           Fraction(favorable_B, total_2) * \
           Fraction(favorable_C, total_3) * \
           Fraction(favorable_D, total_4)

    return prob

# Compute and display
final_probability = calculate_probability()
print(f"🎯 Exact probability in fraction: {final_probability}")
print(f"🧮 Decimal form: {float(final_probability):.10f}")
