import math

def pooled_standard_deviation():
    print("📊 Universal Pooled Standard Deviation Calculator")
    
    # Sample 1
    n1 = int(input("Enter sample size for Group 1 (n1): "))
    s1 = float(input("Enter standard deviation for Group 1 (s1): "))
    
    # Sample 2
    n2 = int(input("Enter sample size for Group 2 (n2): "))
    s2 = float(input("Enter standard deviation for Group 2 (s2): "))
    
    # Calculation
    numerator = (n1 - 1) * (s1 ** 2) + (n2 - 1) * (s2 ** 2)
    denominator = n1 + n2 - 2
    sp = math.sqrt(numerator / denominator)
    
    print(f"\n✅ Pooled Standard Deviation (sp) = {sp:.4f}")

# Run the calculator
pooled_standard_deviation()
