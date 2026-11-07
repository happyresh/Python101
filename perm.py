from itertools import permutations

def restricted_position_assignment():
    print("📌 Position Assignment with Restrictions")

    # Input section
    candidates = input("Enter candidate names separated by commas: ").strip().split(",")
    candidates = [c.strip() for c in candidates if c.strip()]

    pos1 = input("Enter name of Position 1: ").strip()
    pos2 = input("Enter name of Position 2: ").strip()

    restricted_candidate = input("Enter name of candidate with restriction: ").strip()
    preferred_position = input(f"Which position does {restricted_candidate} want? ({pos1}/{pos2}): ").strip()

    if restricted_candidate not in candidates:
        print(f"⚠️ {restricted_candidate} is not in the list of candidates.")
        return

    count = 0

    # Generate all permutations of 2 different candidates
    for perm in permutations(candidates, 2):
        assignment = {pos1: perm[0], pos2: perm[1]}
        
        # Apply restriction
        if restricted_candidate == assignment[pos1]:
            continue  # Restricted candidate is in the wrong position
        if assignment[pos2] == restricted_candidate and preferred_position != pos2:
            continue  # Restricted candidate in wrong position
        count += 1

    print(f"\n✅ Total valid ways to assign positions with restriction: {count}")

# Run the function
restricted_position_assignment()
