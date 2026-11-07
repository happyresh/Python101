import numpy as np
import statistics

def find_interquartile_range():
    """
    A botany instructor obtains examination scores and arranges them in ascending order.
    The first quartile is equal to 40.25. We need to find the interquartile range.
    
    Given scores: 27, 28, ?, 59, 60, 65, 71, 73, 78, 80, 86, 87
    Q1 = 40.25
    """
    
    # Known scores (missing one value)
    known_scores = [27, 28, 59, 60, 65, 71, 73, 78, 80, 86, 87]
    
    # Given information
    q1_given = 40.25
    
    print("Examination Scores Analysis")
    print("=" * 40)
    print(f"Known scores: {known_scores}")
    print(f"Missing score position: 3rd position")
    print(f"Given Q1 = {q1_given}")
    print()
    
    # Since we have 12 total scores, let's work backwards to find the missing score
    # For 12 data points, Q1 position = 0.25 * (12 + 1) = 3.25
    # This means Q1 is between the 3rd and 4th values
    # Q1 = 0.75 * (3rd value) + 0.25 * (4th value)
    
    # We know Q1 = 40.25 and 4th value = 59
    # So: 40.25 = 0.75 * x + 0.25 * 59
    # Solving for x (the missing 3rd value):
    fourth_value = 59
    missing_score = (q1_given - 0.25 * fourth_value) / 0.75
    
    print(f"Calculating missing score:")
    print(f"Q1 = 0.75 * (3rd value) + 0.25 * (4th value)")
    print(f"{q1_given} = 0.75 * x + 0.25 * {fourth_value}")
    print(f"x = ({q1_given} - 0.25 * {fourth_value}) / 0.75")
    print(f"Missing score = {missing_score}")
    print()
    
    # Complete dataset
    complete_scores = [27, 28, missing_score, 59, 60, 65, 71, 73, 78, 80, 86, 87]
    complete_scores.sort()
    
    print(f"Complete dataset: {complete_scores}")
    print()
    
    # Calculate quartiles using numpy
    q1_calc = np.percentile(complete_scores, 25)
    q2_calc = np.percentile(complete_scores, 50)  # median
    q3_calc = np.percentile(complete_scores, 75)
    
    # Calculate interquartile range
    iqr = q3_calc - q1_calc
    
    print("Quartile Calculations:")
    print(f"Q1 (25th percentile) = {q1_calc}")
    print(f"Q2 (50th percentile/median) = {q2_calc}")
    print(f"Q3 (75th percentile) = {q3_calc}")
    print()
    
    print("RESULT:")
    print(f"Interquartile Range (IQR) = Q3 - Q1")
    print(f"IQR = {q3_calc} - {q1_calc} = {iqr}")
    
    return iqr, complete_scores

def verify_calculation():
    """
    Verify our calculation using alternative methods
    """
    print("\n" + "=" * 50)
    print("VERIFICATION")
    print("=" * 50)
    
    # Using the manual quartile calculation method
    complete_scores = [27, 28, 35, 59, 60, 65, 71, 73, 78, 80, 86, 87]
    n = len(complete_scores)
    
    print(f"Dataset size: {n} values")
    print(f"Sorted scores: {complete_scores}")
    
    # Position calculations
    q1_pos = 0.25 * (n + 1)
    q3_pos = 0.75 * (n + 1)
    
    print(f"\nQ1 position: 0.25 * ({n} + 1) = {q1_pos}")
    print(f"Q3 position: 0.75 * ({n} + 1) = {q3_pos}")
    
    # Since positions are not integers, we interpolate
    q1_lower_idx = int(q1_pos) - 1  # Convert to 0-based index
    q1_upper_idx = q1_lower_idx + 1
    q1_weight = q1_pos - int(q1_pos)
    
    q3_lower_idx = int(q3_pos) - 1  # Convert to 0-based index
    q3_upper_idx = q3_lower_idx + 1
    q3_weight = q3_pos - int(q3_pos)
    
    q1_manual = complete_scores[q1_lower_idx] * (1 - q1_weight) + complete_scores[q1_upper_idx] * q1_weight
    q3_manual = complete_scores[q3_lower_idx] * (1 - q3_weight) + complete_scores[q3_upper_idx] * q3_weight
    
    iqr_manual = q3_manual - q1_manual
    
    print(f"\nManual calculation:")
    print(f"Q1 = {complete_scores[q1_lower_idx]} * {1-q1_weight} + {complete_scores[q1_upper_idx]} * {q1_weight} = {q1_manual}")
    print(f"Q3 = {complete_scores[q3_lower_idx]} * {1-q3_weight} + {complete_scores[q3_upper_idx]} * {q3_weight} = {q3_manual}")
    print(f"IQR = {q3_manual} - {q1_manual} = {iqr_manual}")

if __name__ == "__main__":
    iqr, scores = find_interquartile_range()
    verify_calculation()
    
    print(f"\n{'='*50}")
    print("FINAL ANSWER")
    print(f"{'='*50}")
    print(f"The interquartile range is: {iqr}")