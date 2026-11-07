def union_probability():
    print("📊 Universal Union Probability Calculator (P(A or B))")
    
    # Input table
    print("\n➡️ Enter the frequency table row by row. Use this format:")
    print("Header row (e.g. label,O,C,E,A,N):")
    col_labels = input("Column labels: ").strip().split(",")[1:]  # remove row label
    data = {}
    total = 0
    
    print("\nNow enter each row (e.g. Y,82,57,109,31,112):")
    while True:
        row = input("Enter row (or type 'done'): ").strip()
        if row.lower() == "done":
            break
        parts = row.split(",")
        row_label = parts[0]
        values = list(map(int, parts[1:]))
        data[row_label] = dict(zip(col_labels, values))
        total += sum(values)
    
    # Input target row and column
    target_row = input("\nEnter row category (e.g., Y): ").strip()
    target_col = input("Enter column category (e.g., O): ").strip()
    
    # Get values
    row_total = sum(data[target_row].values())
    col_total = sum(data[row][target_col] for row in data)
    intersection = data[target_row][target_col]
    
    # Probabilities
    p_row = row_total / total
    p_col = col_total / total
    p_both = intersection / total
    p_union = p_row + p_col - p_both
    
    print("\n📋 Result Summary:")
    print(f"P({target_row}) = {p_row:.4f}")
    print(f"P({target_col}) = {p_col:.4f}")
    print(f"P({target_row} ∩ {target_col}) = {p_both:.4f}")
    print(f"\n✅ P({target_row} ∪ {target_col}) = {p_union:.4f}")

# Run the calculator
union_probability()
