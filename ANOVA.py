# ANOVA (Analysis of Variance)

from scipy.stats import f_oneway
import pandas as pd

# store the data
veryants = pd.read_csv('/Users/mihai/VS code TEST/Hypothesis Testing/alte fisiere/veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

print(a.head())

# run ANOVA
Fstat, pval = f_oneway(a, b, c)
print(pval)
