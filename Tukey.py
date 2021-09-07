from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# store the data
veryants = pd.read_csv('/Users/mihai/VS code TEST/Hypothesis Testing/alte fisiere/veryants.csv')

# run tukey's test
tukey_results = pairwise_tukeyhsd(veryants.Sale, veryants.Store, 0.05)
print(tukey_results)