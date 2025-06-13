from scipy.stats import binom

def binomial_solver():
    print("🎯 Binomial Distribution Solver")
    print("------------------------------------")
    
    # Get input values
    n = int(input("Enter number of trials (n): "))
    p = float(input("Enter probability of success (p) [0-1]: "))
    
    while True:
        print("\nChoose what you want to calculate:")
        print("a. Probability that X is less than a number (P(X < k))")
        print("b. Probability that X is at least a number (P(X ≥ k))")
        print("c. Mean and Variance")
        print("d. Exit")
        choice = input("Enter your choice (a/b/c/d): ").lower()

        if choice == 'a':
            k = int(input("Enter the number for P(X < k): "))
            prob = sum(binom.pmf(x, n, p) for x in range(k))
            print(f"➡️  P(X < {k}) = {prob:.4f}")

        elif choice == 'b':
            k = int(input("Enter the number for P(X ≥ k): "))
            prob = sum(binom.pmf(x, n, p) for x in range(k, n + 1))
            print(f"➡️  P(X ≥ {k}) = {prob:.4f}")

        elif choice == 'c':
            mean = n * p
            variance = n * p * (1 - p)
            print(f"➡️  Mean = {mean}")
            print(f"➡️  Variance = {variance}")

        elif choice == 'd':
            print("✅ Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run the solver
binomial_solver()
