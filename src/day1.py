'''
Day 1: Descriptive Statistics & NumPy
Concepts: Mean, Median, Mode, Variance, and Standard Deviation.
Practical: Use numpy to calculate these from scratch on a synthetic dataset.
'''

'''
Mean (Average): The "balance point." It’s sensitive to outliers (one ₹10 Cr bungalow will spike the mean).
Median: The "middle" value. It’s robust—outliers don't affect it. If the Mean is much higher than the Median, your data is "Right-Skewed."
Mode: The most frequent value. Great for categorical data (e.g., "Which car color is most popular?").
Variance ($\sigma^2$): Measures how "spread out" the numbers are from the mean.
Standard Deviation ($\sigma$): The square root of variance. It’s in the same units as your data (e.g., Rupees), making it easier to interpret how much a "typical" data point deviates from the average.
'''

'''
In ML, we rarely use for loops for math. We use Vectorization. NumPy allows us to perform operations on entire arrays at once, which is much faster.
'''

import numpy as np
from scipy import stats

def demo_numpy():
    # Step 1: Create a synthetic dataset (Simulating 1000 house prices in Lakhs)
    # We use a normal distribution centered at 50, with a spread of 15
    np.random.seed(42)  # For reproducibility
    prices = np.random.normal(loc=50, scale=15, size=1000)

    # Step 2: Mean calculation (Sum / Count)
    mean_val = np.sum(prices) / len(prices)
    mean_other_way = np.mean(prices)
    print(mean_val, mean_other_way)

    # Step 3: Median (Sort and pick the middle)
    sorted_prices = np.sort(prices)
    n = len(sorted_prices)
    median_val = (sorted_prices[n // 2 - 1] + sorted_prices[n // 2]) / 2

    # Step 4: Variance (Average of squared differences from mean)
    # Formula: sum((x - mean)**2) / n
    variance_val = np.mean((prices - mean_val) ** 2)

    # Step 5: Standard Deviation (Square root of variance)
    std_dev_val = np.sqrt(variance_val)

    print(f"Mean: {mean_val:.2f} Lakhs")
    print(f"Median: {median_val:.2f} Lakhs")
    print(f"Std Dev: {std_dev_val:.2f} Lakhs")

    # Rows: House 1, House 2, House 3
    # Columns: Price, Area
    data = np.array([
        [50, 120],  # House 1
        [60, 150],  # House 2
        [40, 100]  # House 3
    ])

    # Use Case 1: Finding the average for each feature (Columns)
    # We want the mean Price and the mean Area across ALL houses.
    feature_means = np.mean(data, axis=0)
    print(f"Average Price and Area: {feature_means}")
    # Output: [50.0, 123.33]

    # Use Case 2: Finding a row-wise metric
    # (Less common in ML features, but useful for row-level normalization)
    house_averages = np.mean(data, axis=1)
    print(f"Average of values within each house: {house_averages}")
    # Output: [85.0, 105.0, 70.0]

if __name__ == '__main__':
    demo_numpy()