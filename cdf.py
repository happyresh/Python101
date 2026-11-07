def cumulative_range_probability():
    print("📊 Cumulative Probability over a Range (Universal Discrete Calculator)")

    try:
        # Input X and P(X)
        x_values = input("Enter X values separated by commas: ").strip().split(",")
        p_values = input("Enter P(X) values (use ? for one missing), separated by commas: ").strip().split(",")

        x_values = [float(x.strip()) for x in x_values]
        p_values_raw = [p.strip() for p in p_values]
        p_values = []
        missing_index = None

        for i, p in enumerate(p_values_raw):
            if p == "?":
                missing_index = i
                p_values.append(None)
            else:
                p_values.append(float(p))

        # Fill in missing value if one exists
        if missing_index is not None:
            known_sum = sum(p for p in p_values if p is not None)
            missing_prob = 1 - known_sum
            p_values[missing_index] = missing_prob
            print(f"\n🧩 Missing P(X = {x_values[missing_index]}) filled: {missing_prob:.4f}")

        # Check if total is valid
        total_prob = sum(p_values)
        if abs(total_prob - 1.0) > 0.001:
            print(f"\n⚠️ Probabilities do not sum to 1. Total: {total_prob}")
            return

        # Compute expected value
        expected = sum(x * p for x, p in zip(x_values, p_values))
        print(f"📌 Expected Value E[X] = {expected:.4f}")

        # Input range
        lower = float(input("\nEnter LOWER bound (a): "))
        upper = float(input("Enter UPPER bound (b): "))
        include_lower = input("Include LOWER bound? (y/n): ").strip().lower() == 'y'
        include_upper = input("Include UPPER bound? (y/n): ").strip().lower() == 'y'

        # Filter values based on condition
        range_prob = 0
        for x, p in zip(x_values, p_values):
            if ((include_lower and x >= lower) or (not include_lower and x > lower)) and \
               ((include_upper and x <= upper) or (not include_upper and x < upper)):
                range_prob += p

        # Show result
        bounds = f"{'[' if include_lower else '('}{lower}, {upper}{']' if include_upper else ')'}"
        print(f"\n✅ P(X ∈ {bounds}) = {range_prob:.4f}")

    except Exception as e:
        print("❌ Error:", e)

# Run the function
cumulative_range_probability()
