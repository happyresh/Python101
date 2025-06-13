from scipy.stats import bernoulli

def bernoulli_solver():
    print("🎯 Bernoulli Distribution Solver")
    print("-------------------------------")

    # Input probability of success
    while True:
        p = float(input("Enter probability of success (p), 0 ≤ p ≤ 1: "))
        if 0 <= p <= 1:
            break
        print("❌ Invalid input. Try a value between 0 and 1.")

    while True:
        print("\nWhat do you want to calculate?")
        print("a. P(X = x) [0 or 1]")
        print("b. Mean and Variance")
        print("c. Exit")
        choice = input("Enter your choice (a/b/c): ").lower()

        if choice == 'a':
            x = int(input("Enter outcome value (0 or 1): "))
            if x in [0, 1]:
                prob = bernoulli.pmf(x, p)
                print(f"➡️  P(X = {x}) = {prob:.4f}")
            else:
                print("❌ Outcome must be 0 or 1.")
        
        elif choice == 'b':
            mean = p
            variance = p * (1 - p)
            print(f"➡️  Mean = {mean:.4f}")
            print(f"➡️  Variance = {variance:.4f}")

        elif choice == 'c':
            print("✅ Exiting... Stay sharp!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the solver
bernoulli_solver()
