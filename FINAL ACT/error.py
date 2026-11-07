def non_sampling_error():
    print("📌 Non-Sampling Error Calculator")
    
    # Input the incorrect and correct values
    incorrect_value = float(input("Enter the incorrectly recorded value: "))
    correct_value = float(input("Enter the correct value: "))
    
    # Compute the non-sampling error
    error = correct_value - incorrect_value
    
    # Output
    print(f"\n⚠️ Non-Sampling Error: ₱{error:.2f}")
    
    # Optional: Ask if user wants to adjust sample mean
    adjust = input("Do you want to adjust a sample mean? (yes/no): ").lower()
    if adjust == "yes":
        old_mean = float(input("Enter the current sample mean: "))
        n = int(input("Enter the sample size (n): "))
        
        # Remove the effect of the incorrect value and add the correct one
        total = old_mean * n
        adjusted_total = total - incorrect_value + correct_value
        new_mean = adjusted_total / n
        
        print(f"✅ Adjusted Sample Mean: ₱{new_mean:.2f}")

# Run the calculator
non_sampling_error()
