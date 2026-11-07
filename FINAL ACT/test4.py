from scipy.stats import poisson

def poisson_solver():
    print("📚 Poisson Distribution Solver")
    print("------------------------------------")

    # Input mean (λ)
    rate_type = input("Do you want to compute λ from a rate? (yes/no): ").strip().lower()

    if rate_type == "yes":
        percent = float(input("Enter percentage (e.g., 3 for 3%): "))
        total = int(input("Enter total number of items (e.g., pages): "))
        lam = (percent / 100) * total
    else:
        lam = float(input("Enter the average number of events (λ): "))

    while True:
        print("\nWhat would you like to compute?")
        print("1. P(X = k)")
        print("2. P(X ≤ k)")
        print("3. P(X < k)")
        print("4. P(X ≥ k)")
        print("5. P(X > k)")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice in {'1', '2', '3', '4', '5'}:
            k = int(input("Enter the value of k: "))

            if choice == '1':
                prob = poisson.pmf(k, lam)
                print(f"➡️  P(X = {k}) = {prob:.4f}")
            elif choice == '2':
                prob = poisson.cdf(k, lam)
                print(f"➡️  P(X ≤ {k}) = {prob:.4f}")
            elif choice == '3':
                prob = poisson.cdf(k - 1, lam)
                print(f"➡️  P(X < {k}) = {prob:.4f}")
            elif choice == '4':
                prob = 1 - poisson.cdf(k - 1, lam)
                print(f"➡️  P(X ≥ {k}) = {prob:.4f}")
            elif choice == '5':
                prob = 1 - poisson.cdf(k, lam)
                print(f"➡️  P(X > {k}) = {prob:.4f}")

        elif choice == '6':
            print("✅ Exiting Poisson Solver. Thank you, Mr. Recio!")
            break
        else:
            print("❌ Invalid choice. Please choose from 1 to 6.")

# Run the solver
poisson_solver()
