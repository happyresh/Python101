import statistics
from scipy.stats import skew
from collections import Counter

def universal_skewness_analyzer():
    print("\n📊 Universal Skewness and Variability Calculator")
    
    try:
        # Input values
        data = input("Enter numeric values separated by commas: ").strip()
        data = [float(x.strip()) for x in data.split(",") if x.strip()]

        n = len(data)
        mean = statistics.mean(data)
        median = statistics.median(data)
        try:
            mode = statistics.mode(data)
        except:
            mode = "No unique mode"

        variance = statistics.variance(data)
        stdev = statistics.stdev(data)
        data_range = max(data) - min(data)
        fisher_skew = skew(data)  # From scipy.stats

        # Pearson's second coefficient of skewness
        pearson_skew = (3 * (mean - median)) / stdev if stdev != 0 else "Undefined"

        print("\n🔎 Descriptive Statistics:")
        print(f"Count: {n}")
        print(f"Mean: {mean:.4f}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Range: {data_range}")
        print(f"Variance: {variance:.4f}")
        print(f"Standard Deviation: {stdev:.4f}")
        print(f"Pearson's Skewness (2nd): {pearson_skew}")
        print(f"Fisher-Pearson Skewness (scipy): {fisher_skew:.4f}")

        # Optional: Interpretation
        if isinstance(fisher_skew, float):
            if fisher_skew > 0:
                print("📈 Interpretation: Positively skewed (Right-skewed)")
            elif fisher_skew < 0:
                print("📉 Interpretation: Negatively skewed (Left-skewed)")
            else:
                print("📊 Interpretation: Symmetric distribution")

    except Exception as e:
        print("⚠️ Error:", e)

# Run the analyzer
universal_skewness_analyzer()
