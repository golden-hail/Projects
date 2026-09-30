##################################################
# Paired Samples T-Test
##################################################

'''
compare the means where you have two samples of the same observation
comparing results  and after an event
'''

# IMPORT REQUIRED PACKAGES

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm

# CREATE MOCK DATA
before = norm.rvs(loc = 500, scale = 100 , size = 100, random_state = 42).astype(int)

np.random.seed(42)
after = before + np.random.randint(low = -50, high = 75, size = 100)

plt.hist(before, density = True, alpha = 0.5, label = 'before')
plt.hist(after, density = True, alpha = 0.5, label = 'after')
plt.legend()
plt.show()

before_mean = before.mean()
after_mean = after.mean()
print(before_mean,after_mean)

# SET THE HYPOTHESES & ACCEPTANCE CRITERIA 
null_hypothesis = 'The mean of the Before Sample A is equal to the mean of After Sample'
alternate_hypothesis = 'The mean of the Before Sample is different to the mean of After Sample'
acceptance_criteria = 0.05

# EXECUTE THE HYPOTHESIS TEST
t_statistic, p_value = ttest_rel(before, after)
print(t_statistic, p_value)

# PRINT THE RESULTS (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value statistic of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p_value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis and conclude that: {null_hypothesis}")
