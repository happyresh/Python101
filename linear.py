from scipy.stats import skew

# Data: 22 capsule powder contents (in mg)
data = [
    4.73, 5.74,
    6.55, 6.68,
    4.29, 5.31,
    8.78, 7.94,
    6.59, 7.69,
    5.08, 8.33,
    6.70, 7.40,
    7.56, 5.19,
    4.52, 7.12,
    4.18, 6.42,
    7.35, 6.81
]

# Compute skewness
skewness_value = skew(data)

# Output
print(f"📈 Skewness of capsule powder content: {skewness_value:.4f}")
