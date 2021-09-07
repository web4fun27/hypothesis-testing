from scipy.stats import ttest_1samp
import numpy as np

prices = np.genfromtxt("/Users/mihai/VS code TEST/Hypothesis Testing/alte fisiere/prices.csv")
print(prices)

prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))

# use ttest_1samp to calculate pval
tstat, pval = ttest_1samp(prices, 1000)

# print pval
print(pval)