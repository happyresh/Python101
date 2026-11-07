import math
import scipy.stats as stats

def t_test_one_sample(data, population_mean, alpha=0.05):
    n = len(data)
    sample_mean = sum(data) / n
    sample_variance = sum((x - sample_mean) ** 2 for x in data) / (n - 1)
    sample_std_dev = math.sqrt(sample_variance)

    t_statistic = (sample_mean - population_mean) / (sample_std_dev / math.sqrt(n))
    t_critical = stats.t.ppf(1 - alpha / 2, df=n - 1)

    if abs(t_statistic) > t_critical:
        conclusion = "Reject null hypothesis: there is sufficient evidence to support the claim."
    else:
        conclusion = "Fail to reject null hypothesis: there is no sufficient evidence to support the claim."

    return {
        "sample_mean": round(sample_mean, 4),
        "sample_std_dev": round(sample_std_dev, 4),
        "t_statistic": round(t_statistic, 4),
        "t_critical": round(t_critical, 4),
        "conclusion": conclusion
    }

sample_data = [6.14, 10.06, 7.43, 6.88, 5.19,
               7.29, 7.55, 4.08, 5.96, 8.75,
               6.51, 9.23, 7.52, 5.11, 7.62,
               10.37, 5.89, 4.65]

result = t_test_one_sample(sample_data, population_mean=7.20, alpha=0.01)
print(result)
