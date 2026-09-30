##############################################
# Independent Samples T-Test
##############################################
# compares the means of two independent samples to see if there is evidence 
    # that the associated population means are significantly different

# IMPORT REQUIRED PACKAGES

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

# CREATE MOCK DATA
sample_a = norm.rvs(loc = 500, scale = 100 , size = 250, random_state = 42).astype(int)
sample_b = norm.rvs(loc = 550, scale = 150 , size = 100, random_state = 42).astype(int)
    
plt.hist(sample_a, density = True, alpha = 0.5)
plt.hist(sample_b, density = True, alpha = 0.5)
plt.show()

sample_a_mean = sample_a.mean()
sample_b_mean = sample_b.mean()
print(sample_a_mean,sample_b_mean)

# SET THE HYPOTHESES & ACCEPTANCE CRITERIA 

null_hypothesis = 'The mean of Sample A is equal to the mean of Sample B'
alternate_hypothesis = 'The mean of the Sample A is different to the mean of Sample B'
acceptance_criteria = 0.05

# EXECUTE THE HYPOTHESIS TEST
t_statistic, p_value = ttest_ind(sample_a, sample_b)
print(t_statistic, p_value)

# PRINT THE RESULTS (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value statistic of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p_value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis and conclude that: {null_hypothesis}")

## Independent T-Test assumes that the two populations will have distributions with equal variance 

'''
## WELCH'S T-TEST
#### Welch's T-Test: Apply this one by default
    # more reliable than the regular independent T test whenever sample sizes and variances 
    # are unequal between groups and it gives the same result when sample sizes and variances are equal 
    
## In Welch's case: We are less confident in the difference between our two samples
'''

# EXECUTE THE HYPOTHESIS TEST
t_statistic, p_value = ttest_ind(sample_a, sample_b, equal_var = False)
print(t_statistic, p_value)

# PRINT THE RESULTS (p-value)
if p_value <= acceptance_criteria:
    print(f"As our p_value statistic of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p_value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis and conclude that: {null_hypothesis}")

