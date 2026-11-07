from scipy.stats import norm

def find_z0_from_area():
    print("🎯 Universal Z-score Finder for Area Between Two Z-values (Standard Normal)")

    try:
        z1 = float(input("Enter the known z-value (z1): "))
        area_between = float(input("Enter the area between z1 and z0 (as decimal, e.g., 0.0538): "))

        # Step 1: Find cumulative area up to z1
        cumulative_z1 = norm.cdf(z1)

        # Step 2: Add the area_between to cumulative_z1
        cumulative_z0 = cumulative_z1 + area_between

        # Step 3: Get z0 using the inverse CDF
        z0 = norm.ppf(cumulative_z0)

        print(f"\n✅ z0 such that the area between {z1} and z0 is {area_between:.4f}:")
        print(f"z0 = {z0:.4f}")
    except:
        print("⚠️ Invalid input. Please enter valid decimal numbers.")

# Run the function
find_z0_from_area()
