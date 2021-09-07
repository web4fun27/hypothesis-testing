# Import libraries
import pandas as pd
import numpy as np

# Brian: We are trying to get users to purchase a small FarmBurg upgrade package. 
# It’s called a microtransaction. We’re not sure how much to charge for it, 
# so we tested three different price points: 
# $0.99 (group 'A'), $1.99 (group 'B'), and $4.99 (group 'C'). 

# Brian: Hmm. I guess that we need to generate a minimum of $1000 in revenue per week 
# in order to justify this project.


# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('/Users/mihai/VS code TEST/Hypothesis Testing/Projects/Analyzing Farmburg_s A-B Test/clicks.csv')

# Inspect the dataframe
print(abdata.head())

# Create a contingency table with pd.crosstab
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)

# Print the contingency table
print(Xtab)

# Import chi2_contingency module
from scipy.stats import chi2_contingency

# Calculate the p-value
chi2, pval, dof, expected = chi2_contingency(Xtab)

# Print the p-value
print(pval)

# Determine if the p-value is significant
is_significant = True

# Calculate and print the number of visits
num_visits = len(abdata)

# Print the number of visits
print(num_visits)

# Calculate the purchase rate needed at 0.99
num_sales_needed_099 = 1000/0.99
p_sales_needed_099 = num_sales_needed_099/num_visits

# Print the purchase rate needed at 0.99
print(p_sales_needed_099)

# Calculate the purchase rate needed at 1.99
num_sales_needed_199 = 1000/1.99
p_sales_needed_199 = num_sales_needed_199/num_visits

# Print the purchase rate needed at 1.99
print(p_sales_needed_199)

# Calculate the purchase rate needed at 4.99
num_sales_needed_499 = 1000/4.99
p_sales_needed_499 = num_sales_needed_499/num_visits

# Print the purchase rate needed at 4.99
print(p_sales_needed_499)

# Calculate samp size & sales for 0.99 price point
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 0.99 price point
print(samp_size_099)
print(sales_099)

# Calculate samp size & sales for 1.99 price point
samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 1.99 price point
print(samp_size_199)
print(sales_199)

# Calculate samp size & sales for 4.99 price point
samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

# Print samp size & sales for 4.99 price point
print(samp_size_499)
print(sales_499)

# Import the binom_test module
from scipy.stats import binom_test

# Calculate the p-value for Group A
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')

# Print the p-value for Group A
print(pvalueA)

# Calculate the p-value for Group B
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')

# Print the p-value for Group B
print(pvalueB)

# Calculate the p-value for Group C
pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')

# Print the p-value for Group C
print(pvalueC)

# Set the correct value for the final answer variable
final_answer = '4.99'

# Print the chosen price group
print(final_answer)

print("pvalue-C is the only p-value below the threshold of 0.05. \
Therefore, the C group is the only group where we would conclude \
that the purchase rate is significantly higher than the target \
needed to reach $1000 revenue per week. Therefore, \
Brian should charge $4.99 for the upgrade.")