import numpy as np
import pandas as pd
from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(4, 10, .5)
print("2sided p_value= ", p_value_2sided)

p_value_1sided = binom_test(2, 10, .5, alternative = 'less')
print("1sided less p_value= ", p_value_1sided)

p_value_1sided = binom_test(19, 2000, .01, alternative = 'greater')
print("1sided greater p_value= ", p_value_1sided)