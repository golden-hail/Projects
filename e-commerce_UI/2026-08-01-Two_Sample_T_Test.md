---
layout: post
title: UI A/B Test & Conversion Rate Optimization
image: "/posts/AB_testing.jpg"
tags: [AB Testing, Hypothesis Testing, Z-Test, Python]
---

In this project, we'll be running an A/B test to determine whether the new purchasing checkout UI for our e-commerce website is leading to more customer purchases when it's time to checkout.

We will do this through applying the ______ to measure the significance of the difference in signups between 2 groups of customers. 2 Sample T Test with Z test of proportions 

# Table of contents?

___

# Project Overview  <a name="overview-main"></a>

<br>
### Context <a name="overview-context"></a>

An e-commerce platform recently launched a redesigned payment flow on their UI to boost checkout conversions. These checkout conversions occur from when the item is added to cart to the items bought on that date(explain / move this later?)

You need to determine if the new UI statistically outperforms the control group 
without negatively impacting order total values.

Engineering Angle: Focus on performance metrics, drop-off pipelines, and user behavioral flows.

A $+18.92\%$ jump looks incredible on paper. But before an engineering or executive team spends money and resources updating the live site for 100% of users, they will ask: "How do we know this isn't just a 30-day random spike in traffic behavior?"

<br>

### Actions <a name="overview-actions"></a>

-data at a glance (with Cart Conversion Rate (Checkout UI Efficiency))
    -Control: 40.21% of people who added items to their cart bought them.
    -Test: 59.13% of people who added items to their cart bought them.

Conclusion so far: The new payment UI got significantly more people through checkout!

Average Order Value (AOV / Spend per Purchase):$$\frac{\text{Total Spend}}{\text{Total Purchases}}$$Control: $4.41 spent per purchase.Test: $4.92 spent per purchase.Conclusion so far: The new UI didn't hurt spending—users actually spent slightly more per transaction!

Step 3: Run the Statistical Tests (Phase 3) Now you prove that the jump from 40.21% to 59.13% isn't just random luck.For Conversion Rate: You run a Two-Sample Z-Test for Proportions using statsmodels.For Spend / AOV: You check if the spending data is normal using a Shapiro-Wilk test, then run a $t$-test or Mann-Whitney U test in scipy.stats.Goal: If the $p$-value from these tests is less than 0.05, you can officially say: "The improvement is statistically significant."

Step 4: Make the Business Recommendation (Phase 4)You summarize your findings into a 3-bullet recommendation for management:Cart-to-Purchase conversion increased by ~19 percentage points with the new UI.Average Order Value increased by $0.51 per order.Recommendation: Roll out the redesigned payment flow to 100% of website users.

<br>

### Results & Discussion <a name="overview-results"></a>



___

# Concept Overview  <a name="concept-overview"></a>
<br>
### A/B Testing

An A/B test takes two randomized groups, A and B, and provides them with different experiences. In the A/B test, we measure the response of each group to understand the impact each experience had on the response. These insights can help drive business decisions in the future.

For example, a company may post 2 different pictures advertising the same product on their website. With an A/B test, we could look to measure if the picture used in the ad significantly impacted the number of users who clicked on the ad. If one ad yielded significantly more clicks, the business can use this data when thinking about what characteristics got the user to click and incorporate those features into future ads.

<br>
### Hypothesis Testing



<br>
#### Z-Test for Proportions

Why run the Z-Test for proportions here? Well, we have 2 sample sets each with a different experience (ie. the new or legacy UI). Since we want to see if there is a statistically significant difference between checkout/purchase rates between the control group who got the legacy experience and the  

___

# Data Overview & Preparation  <a name="data-overview"></a>

Import 2 groups of data, control group with the original UI and the test group with the new UI. This data contains sales metrics on each unique day during the data collection.


'''python
import pandas as pd

control = pd.read_csv('control_group.csv', sep = ';')
test = pd.read_csv('test_group.csv', sep = ';')

control = control.dropna()
test = test.dropna()
'''

!!At a first glance, it seems the data...
in the test group with the new UI, 59.128% committed to purchasing their carted items
in the control group, with the legacy UI, 40.215% committed to buying their products 


___

# Applying the Z-Test for Proportions <a name="Z-test-application"></a>

<br>

#### State Hypotheses & Significance Level For Test

To kick off our Hypothesis Test, we'll need to define our **Null Hypothesis**, our **Alternate Hypothesis**, and our **Significance Level**. (See more on these terms in the *Concept Overview* section above)

For our significance level, we'll be using the commonly used value of 0.05 (or 5%).

* null_hypothesis: There is no significant relationship between the UI version and the sales conversion rate. They are independent.
* alternate_hypothesis: There is a relationship between the UI version and the sales conversion rate. They are not independent.
* acceptance_criteria: 0.05

<br>

#### Calculate Observed Frequencies & Expected Frequencies?

For Conversion Rate..

'''python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

purchases = [test["# of Purchase"].sum(), control["# of Purchase"].sum()]
carts = [test["# of Add to Cart"].sum(), control["# of Add to Cart"].sum()]

z_stat, p_val = proportions_ztest(
    count=purchases, nobs=carts, alternative="larger"
)

print(f"Z-statistic: {z_stat:.4f}")
print(f"p-value:     {p_val}")
'''

Z-statistic: 47.1959
p-value:     0.0

!!! Interpret results
Decision Rule:If $p \text{-value} < 0.05$, Reject $H_0$.If $p \text{-value} \ge 0.05$, Fail to Reject $H_0$.

Conclusion: Because $p \approx 0$ (which is far below $0.05$), we reject the null hypothesis. The $18.92\%$ jump in cart conversion rate is statistically significant and virtually impossible to have happened by random chance.

The $Z$-statistic (or $Z$-score) is the single standardized score that measures how far apart your two groups are, expressed in units of expected random noise (standard errors).While the $p$-value tells you if a difference is statistically significant, the $Z$-statistic tells you how strong and extreme that difference is relative to random variation.

___

# Applying Shapiro-Wilk to Assess for Data Normality


# Applying T-Test (With Plot)

___

# Analyzing The Results <a name="chi-square-results"></a>

-data at a glance (with Cart Conversion Rate (Checkout UI Efficiency))
    -Control: 40.21% of people who added items to their cart bought them.
    -Test: 59.13% of people who added items to their cart bought them.

Conclusion so far: The new payment UI got significantly more people through checkout!

Then after running the Z-Test for proportions, 

___

# Discussion <a name="discussion"></a>

