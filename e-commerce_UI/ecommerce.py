'''
Project 1: E-Commerce UI A/B Test & Conversion Rate OptimizationBusiness 

$Statistical Framework & PipelineNormality & Variance Check: Perform a Shapiro-Wilk test and 
Levene's test on spending data to check assumptions. 
Proportion Test (Two-Sample Z-Test): Compare conversion rates between control (A) and treatment (B).

Continuous Metric Test:
If normal: Two-Sample Independent Student's t-test for AOV.
If skewed (common in e-commerce spend): Mann-Whitney U Test (non-parametric).

Recommended DatasetsKaggle: Search for A/B Testing Dataset by Amir Motefaker.

'''

import pandas as pd

# Import 2 groups of data, control group with the original UI
    # and the test group with the new UI
control = pd.read_csv('control_group.csv', sep = ';').dropna()
test = pd.read_csv('test_group.csv', sep = ';').dropna() 

control = control.dropna()
test = test.dropna()

# Compute totals for Control and Test groups
ctrl_spend = control['Spend [USD]'].sum()
test_spend = test['Spend [USD]'].sum()

ctrl_purchases = control['# of Purchase'].sum()
test_purchases = test['# of Purchase'].sum()

# Conversion rates and totals spent per purchase
ctrl_conversion_rate = round(control['# of Purchase'].sum() / control['# of Add to Cart'].sum() * 100, 3)
test_conversion_rate = round(test['# of Purchase'].sum() / test['# of Add to Cart'].sum() * 100, 3)

relative_lift = (test_conversion_rate - ctrl_conversion_rate)/ctrl_conversion_rate * 100

print(f'Control Group Conversion Rate = {ctrl_conversion_rate}%')
print(f'Test Group Conversion Rate = {test_conversion_rate}%')
print(f'Relative Lift = {relative_lift:.2f}%')

###############$$$$$$$$
# convert to $$$ to get the interest of business
ctrl_AOV = round(control['Spend [USD]'].sum()/control['# of Purchase'].sum(), 2)
test_AOV = round(test['Spend [USD]'].sum()/test['# of Purchase'].sum(), 2)

print(f'Control AOV = ${ctrl_AOV}')
print(f'Test AOV = ${test_AOV}')

#######################
# STEP 1: Z-Test For Proportions
#######################

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

purchases = [test["# of Purchase"].sum(), control["# of Purchase"].sum()]
carts = [test["# of Add to Cart"].sum(), control["# of Add to Cart"].sum()]

z_stat, p_val = proportions_ztest(
    count=purchases, nobs=carts, alternative="larger"
)

print(f"Z-statistic: {z_stat:.4f}")
print(f"p-value:     {p_val:.5f}")

#######################
# STEP 2: Shapiro Wilk Test
#######################

'''
Step 1: Set Up Your HypothesesUnlike the Z-test for proportions, 
the null hypothesis for a normality test is about matching a normal curve:
    Null Hypothesis ($H_0$): The data is normally distributed.
    Alternative Hypothesis ($H_1$): The data is NOT normally distributed.
    Important Rule: You want a high $p$-value ($p \ge 0.05$) if you hope to prove your data is normal.
'''

from scipy import stats

# Calculate AOV
control["AOV"] = control["Spend [USD]"] / control["# of Purchase"]
test["AOV"] = test["Spend [USD]"] / test["# of Purchase"]

# Run Shapiro-Wilk on AOV
stat_ctrl, p_ctrl = stats.shapiro(control["AOV"])
stat_test, p_test = stats.shapiro(test["AOV"])

print(f"Control AOV - W Stat: {stat_ctrl:.4f}, p-value: {p_ctrl:.4f}")
print(f"Test AOV - W Stat: {stat_test:.4f}, p-value: {p_test:.4f}")

## Monte Carlo W stat: 
import numpy as np
from scipy import stats

# Set your sample size and alpha level
N = 30
alpha = 0.05
num_simulations = 100_000  # Generate 100,000 normal samples

# 1. Generate 100,000 random samples drawn from a perfectly normal distribution
simulated_samples = np.random.normal(loc=0, scale=1, size=(num_simulations, N))

# 2. Compute the Shapiro-Wilk W statistic for each simulated sample
w_stats = np.apply_along_axis(lambda x: stats.shapiro(x).statistic, axis=1, arr=simulated_samples)

# 3. Get the 5th percentile (alpha = 0.05 cutoff)
w_crit = np.percentile(w_stats, alpha * 100)

print(f"Calculated W_crit for N={N} at alpha={alpha}: {w_crit:.4f}")
# Output: ~0.9270

#######################
# STEP 3: Mann-Whitney U Test
#######################

control["AOV"] = control["Spend [USD]"] / control["# of Purchase"]
test["AOV"] = test["Spend [USD]"] / test["# of Purchase"]

# 3. Perform Mann-Whitney U Test
mwu_stat, mwu_p = stats.mannwhitneyu(
    test["AOV"], control["AOV"], alternative="two-sided"
)

print("--- MANN-WHITNEY U TEST RESULTS ---")
print(f"U-statistic: {mwu_stat:.4f}")
print(f"p-value:     {mwu_p:.4f}")

#######################
# STEP 4: Welch's T Test
#######################
# Perform Welch's Two-Sample t-test (equal_var=False)
welch_stat, welch_p = stats.ttest_ind(
    test["AOV"], control["AOV"], equal_var=False
)

print(f"t-statistic: {welch_stat:.4f}")
print(f"p-value:     {welch_p:.4f}")

'''
For Spend / AOV: You check if the spending data 
is normal using a Shapiro-Wilk test, 

then run a $t$-test or Mann-Whitney U test in scipy.stats.

Goal: If the $p$-value from these tests is less than 0.05, 
you can officially say: "The improvement is statistically significant."

### Discussion
# # click-to-purchase (maybe use later? to see ad engagement?)
# Spend [USD]
'''

'''
Did the new payment UI get more people to buy? (Conversion Rate) - ind sample t test

Did people spend less money when they used the new UI? (Average Order Value) one sample t test? 

Is the difference real, or just a random fluke? (Statistical Significance) z test proportions?

┌─────────────────────────────────────────────────────────┐
│ PHASE 1: Look at the Raw Data (Exploration)             │
│ "What columns do I have, and how many users are there?" │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: Calculate the Basics (Simple Averages)         │
│ "What is the conversion rate for Control vs. Test?"    │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: Run the Statistics (The Validation)            │
│ "Is the difference big enough to trust?"                │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 4: Make a Recommendation (Business Impact)        │
│ "Should the company launch the new UI to everyone?"     │
└─────────────────────────────────────────────────────────┘
'''

# 3. Calculate Metrics
# print("--- CONTROL GROUP METRICS ---")
# print(
#     f"Click-to-Purchase Conv Rate: {(ctrl_purchases / ctrl_clicks) * 100:.2f}%"
# )
# print(f"Average Order Value (AOV):  ${ctrl_spend / ctrl_purchases:.2f}")
# print(f"Spend per Website Click:    ${ctrl_spend / ctrl_clicks:.2f}\n")

# print("--- TEST GROUP METRICS ---")
# print(
#     f"Click-to-Purchase Conv Rate: {(test_purchases / test_clicks) * 100:.2f}%"
# )
# print(f"Average Order Value (AOV):  ${test_spend / test_purchases:.2f}")
# print(f"Spend per Website Click:    ${test_spend / test_clicks:.2f}")

