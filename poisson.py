from scipy.stats import poisson

def poisson_solver():
    print("🎯 Poisson Distribution Solver")
    print("-------------------------------")
    
    # Input mean (lambda)
    lamb = float(input("Enter the average rate of success (λ): "))

    while True:
        print("\nWhat do you want to calculate?")
        print("a. P(X = k)")
        print("b. P(X ≤ k)")
        print("c. P(X ≥ k)")
        print("d. Mean and Variance")
        print("e. Exit")
        choice = input("Enter your choice (a/b/c/d/e): ").lower()

        if choice in ['a', 'b', 'c']:
            k = int(input("Enter number of occurrences (k): "))

            if choice == 'a':
                prob = poisson.pmf(k, lamb)
                print(f"➡️  P(X = {k}) = {prob:.4f}")

            elif choice == 'b':
                prob = poisson.cdf(k, lamb)
                print(f"➡️  P(X ≤ {k}) = {prob:.4f}")

            elif choice == 'c':
                prob = 1 - poisson.cdf(k - 1, lamb)
                print(f"➡️  P(X ≥ {k}) = {prob:.4f}")

        elif choice == 'd':
            print(f"➡️  Mean = {lamb}")
            print(f"➡️  Variance = {lamb}")

        elif choice == 'e':
            print("✅ Exiting... Happy solving!")
            break

        else:
            print("❌ Invalid choice. Try again.")

# Run the solver
poisson_solver()
