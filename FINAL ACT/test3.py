from scipy.stats import binom

def binomial_solver():
    print("📊 Welcome to Mr. Recio’s Binomial Probability Calculator!")
    print("----------------------------------------------------------")

    # Input: n and p
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success (p) [0-1]: "))

    while True:
        print("\nChoose an option:")
        print("1. P(X = k)")
        print("2. P(X ≤ k)")
        print("3. P(X < k)")
        print("4. P(X ≥ k)")
        print("5. P(X > k)")
        print("6. Mean and Variance")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice in {'1', '2', '3', '4', '5'}:
            k = int(input("Enter the value of k: "))

            if choice == '1':
                prob = binom.pmf(k, n, p)
                print(f"➡️  P(X = {k}) = {prob:.4f}")

            elif choice == '2':
                prob = binom.cdf(k, n, p)
                print(f"➡️  P(X ≤ {k}) = {prob:.4f}")

            elif choice == '3':
                prob = binom.cdf(k - 1, n, p)
                print(f"➡️  P(X < {k}) = {prob:.4f}")

            elif choice == '4':
                prob = 1 - binom.cdf(k - 1, n, p)
                print(f"➡️  P(X ≥ {k}) = {prob:.4f}")

            elif choice == '5':
                prob = 1 - binom.cdf(k, n, p)
                print(f"➡️  P(X > {k}) = {prob:.4f}")

        elif choice == '6':
            mean = n * p
            variance = n * p * (1 - p)
            print(f"📐 Mean = {mean:.2f}")
            print(f"📊 Variance = {variance:.2f}")

        elif choice == '7':
            print("✅ Exiting... Thank you for using this solver, Mr. Recio!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option (1-7).")

# Run the solver
binomial_solver()
