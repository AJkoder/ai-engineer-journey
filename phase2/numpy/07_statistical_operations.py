import numpy as np

scores = np.array([60, 70, 75, 80, 95])

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard deviation:", np.std(scores))
print("Variance:", np.var(scores))
print("25th percentile:", np.percentile(scores, 25))
print("75th percentile:", np.percentile(scores, 75))

# Compare how an outlier affects mean and median.
with_outlier = np.array([60, 70, 75, 80, 500])

print("\nWith an outlier:")
print("Mean:", np.mean(with_outlier))
print("Median:", np.median(with_outlier))

# Sample standard deviation uses ddof=1.
print("Sample standard deviation:", np.std(scores, ddof=1))
