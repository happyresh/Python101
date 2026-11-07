import scipy.stats as stats

def paired_t_test(before, after, alpha=0.01):
    # Step 1: Calculate the differences
    differences = [after[i] - before[i] for i in range(len(before))]

    # Step 2: Perform paired t-test
    t_statistic, p_value = stats.ttest_rel(after, before)

    # Step 3: Since we are doing a one-tailed test (H1: μd > 0), divide the p-value by 2
    one_tailed_p = p_value / 2

    # Step 3.5: Calculate critical value for one-tailed test
    degrees_of_freedom = len(before) - 1
    critical_value = stats.t.ppf(1 - alpha, degrees_of_freedom)

    # Step 4: Decision rule
    if t_statistic > 0 and one_tailed_p < alpha:
        decision = "Reject the null hypothesis. ✅ There is sufficient evidence to support the claim that productivity increased."
    else:
        decision = "Do NOT reject the null hypothesis. ❌ There is not enough evidence to support the claim that productivity increased."

    return t_statistic, one_tailed_p, critical_value, decision

# 🧑‍💻 Input: Before and After values
before = [92, 86, 91, 95, 76, 84, 92, 93, 86, 79, 85, 88, 83, 90, 89, 84, 75, 84]
after  = [97, 88, 90, 97, 81, 80, 95, 87, 91, 83, 90, 89, 78, 96, 92, 88, 86, 83]

# Significance level (1%)
alpha = 0.01

# Run the test
t_stat, p_val, crit_val, result = paired_t_test(before, after, alpha)

# 🖨️ Output
print("📊 Paired Sample t-Test Results (One-tailed)\n")
print(f"T-Statistic: {t_stat}")
print(f"Critical Value: {crit_val}")
print(f"One-tailed P-Value: {p_val}")
print(f"Decision: {result}")
