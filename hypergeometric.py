from scipy.stats import hypergeom

def hypergeometric_solver():
    print("🎯 Hypergeometric Distribution Solver")
    print("------------------------------------")
    
    # Input parameters
    N = int(input("Enter total population size (N): "))
    K = int(input("Enter number of successes in population (K): "))
    n = int(input("Enter number of draws (n): "))

    while True:
        print("\nWhat do you want to calculate?")
        print("a. P(X = k)")
        print("b. P(X ≤ k)")
        print("c. P(X ≥ k)")
        print("d. Mean and Variance")
        print("e. Exit")
        choice = input("Enter your choice (a/b/c/d/e): ").lower()

        if choice in ['a', 'b', 'c']:
            k = int(input("Enter number of observed successes (k): "))
            rv = hypergeom(N, K, n)

            if choice == 'a':
                prob = rv.pmf(k)
                print(f"➡️  P(X = {k}) = {prob:.4f}")
            elif choice == 'b':
                prob = rv.cdf(k)
                print(f"➡️  P(X ≤ {k}) = {prob:.4f}")
            elif choice == 'c':
                prob = 1 - rv.cdf(k - 1)
                print(f"➡️  P(X ≥ {k}) = {prob:.4f}")

        elif choice == 'd':
            mean = n * (K / N)
            variance = n * (K / N) * ((N - K) / N) * ((N - n) / (N - 1))
            print(f"➡️  Mean = {mean:.4f}")
            print(f"➡️  Variance = {variance:.4f}")

        elif choice == 'e':
            print("✅ Exiting... Good luck solving!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the solver
hypergeometric_solver()
