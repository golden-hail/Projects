---
layout: post
title: Title and image and tag??
image: "/posts/checkout_UI.jpg"
tags: [AB Testing, Hypothesis Testing, Z-Test, Shapiro-Wilk, Mann-Whitney U, Python]
---

Comparitive modeling project -

You will compare a parametric, interpretable model (Regression) 
against a non-parametric, instance-based model (KNN).

Identify high-risk churn profiles, quantify customer lifetime revenue drivers, benchmark similar customer behavior, and cluster account types to design targeted retention strategies.

* Identify high-risk churn profiles with logistic regression

quantify customer lifetime revenue drivers

benchmark similar customer behavior

cluster account types to design targeted retention strategies
___

# Table of Contents

- [00. Project Overview](#overview-main)
    - [Context](#overview-context)
    - [Actions](#overview-actions)
    - [Results & Discussion](#overview-results)
- [01. Data Overview & Preparation](#data-overview)
- [02. Applying Z-Test for Proportions](#z-test-application)
- [03. Applying Shapiro-Wilk to Assess for Data Normality](#shapiro-wilk)
- [04. Applying Mann-Whitney U Test](#mann-whitney)
- [05. Analyzing The Results](#Z-test-results)
- [06. Discussion](#discussion)

___

# Project Overview  <a name="overview-main"></a>
<br>
### Context <a name="overview-context"></a>

IBM Telco has data on customers, including those who have left (churn). We want to predict who is a flight risk / most likely to churn and give up on our services. 

Domain: Business Analytics / Subscription Services
Project Title: Predicting Customer Churn and LTV: Logistic Regression vs. K-Nearest Neighbors for Retention Strategy
Business Problem

A subscription business wants to identify customers at risk of cancelling their membership (Churn) and estimate their overall spend (Lifetime Value). The goal is to provide actionable recommendations for retention teams while evaluating model trade-offs between interpretability (Regression) and local pattern recognition (KNN).

<br>

### Actions <a name="overview-actions"></a>

Project Structure & Methodology
1. Linear Regression vs. KNN Regressor (Numerical Target)
	• Target Variable: Total Customer Spend or Customer Lifetime Value (LTV).
	• Linear Regression Role: Quantifies the exact relationship between features (e.g., tenure, monthly charges) and spend, offering clear business coefficients.
	• KNN Regressor Role: Captures non-linear local patterns by averaging the spend of similar customer profiles.
2. Logistic Regression vs. KNN Classifier (Binary Classification Target)
	• Target Variable: Churn Status (1 = Churned, 0 = Retained).
	• Logistic Regression Role: Outputs log-odds and odds ratios to show which factors directly drive churn probability.
	• KNN Classifier Role: Classifies customers based on the churn behavior of their k-most similar peers in the feature space.
3. Key Analytics Highlights for Your Portfolio
	• Preprocessing: Feature scaling (StandardScaler) is critical for KNN and regularized regression—demonstrate how feature ranges impact distance metrics.
	• Model Evaluation:
		○ Regression: Compare R^2, MAE, and RMSE.
		○ Classification: Compare Accuracy, Precision, Recall, F1-Score, and ROC-AUC curves.
Business Insights: Explain why a company might prefer Logistic Regression for executive reporting (interpretability) even if KNN achieves slightly higher accuracy.

<br>

### Results & Discussion <a name="overview-results"></a>

Key Takeaways for Your Portfolio Presentation
	• Highlight Trade-offs: Parametric models (Linear/Logistic Regression) assume explicit relationships and yield interpretable coefficients. Non-parametric models (KNN) make fewer assumptions but require scaling and incur higher memory/computation costs at prediction time.
	• Data Preprocessing Focus: Document how scaling changed KNN performance versus Linear Regression to show strong data engineering fundamentals.
Executive Summary: Include a 1-page summary explaining the model findings in terms of business impact (e.g., "Increasing tenure by 12 months reduces churn odds by 34% according to Logistic Regression").

___

# Data Overview & Preparation  <a name="data-overview"></a>
<br>


You don't have to ignore location entirely! In fact, mentioning it in your Exploratory Data Analysis (EDA) section makes your project look much more thorough.

1) Drop the column for Tenure Months == 0 as there is no data associated with these customers yet

```python
raw_data = raw_data[raw_data['Tenure Months'] != 0]
```

Interested in the following columns for our analysis:

* 'Total charges' (to see if they're well paying customers/ financial impact of churn) 
* CLTV (Customer Lifetime Value): Ranges from $2,000 to $8,000
* Tenure Months: Ranges from 0 to 72
* Monthly Charges: Ranges from $18 to $118
* Service_Count: Ranges from 0 to 6 
* Contract: categorical - either Monthly,./...

2) Service_count: 
'''
## Get a count of add-on services that each customer has in addition to their base..
    # More difficult for customers with greater number of services to leave/switch
'''

xtra_servs = ['Online Security', 'Online Backup', 'Device Protection', 
              'Tech Support', 'Streaming TV', 'Streaming Movies']

# Creates a True/False column for 'Yes' values and sums across rows (axis=1)
raw_data['addon_service_count'] = (raw_data[xtra_servs] == 'Yes').sum(axis=1)


3) Contract: catagorical data to be onehotencoded for ML (dummy variable trap??)

4) standardize other applicable data

___

# Applying Z-Test for Proportions <a name="z-test-application"></a>

<br>

### State Hypotheses & Significance Level For Test

To kick off our Z-Test, we'll need to define our **Null Hypothesis**, our **Alternate Hypothesis**, and our **Significance Level**. For our significance level, we'll be using the commonly used value of 0.05 (or 5%), which will be carried through for all subsequent tests.

* **Null Hypothesis:** There is no significant relationship between the checkout UI version and the sales conversion rate. They are independent.
* **Alternate Hypothesis:** There is a relationship between the checkout UI version and the sales conversion rate. They are not independent.
* **Significance Level:** 0.05

<br>

## Calculating the P-Value

We want to look at if the new UI led to a significant increase in conversion rate, from items added to the cart to the purchase step.

```
* If p-value >= 0.05: Fail to reject the null hypothesis. UI version and conversion rate are statistically independent
* If p-value < 0.05: Reject the null hypothesis in favor of the alternate
```

To do this, we will `statsmodels.stats.proportion` library was used to import the `proportion_ztest` algorithm, to run our Z-Test. The results of this test will provide a p-value to be compared against our significance level.

<u>Inputs of the proportions_ztest:</u>  
--`count` represents the amount of successes for each dataset: it will be defined as the number of total purchases from each dataset.  
--`nobs (ie. Number of Observations)` will be the number of items added to carts.  
--`alternative`, looking if the % of signups is significantly higher, or *larger*

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

purchases = [test["# of Purchase"].sum(), control["# of Purchase"].sum()]
carts = [test["# of Add to Cart"].sum(), control["# of Add to Cart"].sum()]

z_stat, p_val = proportions_ztest(
    count=purchases, nobs=carts, alternative="larger"
)

print(f"Z-statistic: {z_stat:.4f}")
print(f"p-value:     {p_val:.4f}")

>> Z-statistic: 47.1959
>> p-value:     0.0000
```

Our calculated p-value of 0.0000 is less than our set significance level of 0.05, which provides evidence to reject the null hypothesis in favor of the alternate. The 18.92% jump in cart-to-purchase conversion rate is statistically significant and virtually impossible to have happened by random chance!

___

# Applying Shapiro-Wilk to Assess for Data Normality <a name="shapiro-wilk"></a>

<br>

To assess the effect the UI version had on the Average Order Value (AOV), we first need to determine whether to run a parametric or a non-parametric test through another hypothesis test known as the Shapiro-Wilk test. 

* **Null Hypothesis:** The daily AOV data in both groups is normally distributed
* **Alternate Hypothesis:** The daily AOV data in both groups is not normally distributed
* **Significance Level:** 0.05

Parametric tests such as the standard two-sample *t*-test rely on the assumption of data normality to calculate standard errors and p-values; violating this assumption risks inflating Type I error rates. Running the Shapiro-Wilk test allows us to verify the data structure before selecting a model. 

## Calculating the P-Value

```
* If p-value >= 0.05: The daily AOV in both groups is normally distributed. Run Welch's *t*-test to assess statistical significance
* If p-value < 0.05: The daily AOV data is not normally distributed. Run the Mann Whitney U to assess statistical significance
```

We'll acquire the Shapiro-Wilk p-value outputs with the `scipy` library `stats` module.

```python
from scipy import stats

# Calculate AOV
control["AOV"] = control["Spend [USD]"] / control["# of Purchase"]
test["AOV"] = test["Spend [USD]"] / test["# of Purchase"]

# Run Shapiro-Wilk on AOV
stat_ctrl, p_ctrl = stats.shapiro(control["AOV"])
stat_test, p_test = stats.shapiro(test["AOV"])

print(f"Control AOV - W Stat: {stat_ctrl:.4f}, p-value: {p_ctrl:.4f}")
print(f"Test AOV - W Stat: {stat_test:.4f}, p-value: {p_test:.4f}")

>> Control AOV - W Stat: 0.9132, p-value: 0.0206
>> Test AOV - W Stat: 0.8966, p-value: 0.0069
```

The p-values returned from the Shapiro-Wilk test are less than the significance level of 0.05 for both groups, indicating that the AOV data is not normally distributed.

Consequently, we proceed with the non-parametric Mann-Whitney U test, which compares distribution ranks rather than sample means and requires no distributional assumptions.

___

# Applying Mann-Whitney U Test <a name="mann-whitney"></a>

We've now determined to run the Mann-Whitney U Test to assess our AOV between the control and test data.

* **Null Hypothesis:** There is no statistical difference in the distribution of daily AOV between the Control and Test groups
* **Alternate Hypothesis:** There is a statistically significant difference in the distribution of daily AOV between the Control and Test groups
* **Significance Level:** 0.05

## Calculating the P-Value

```
* If p-value >= 0.05: There is statistically no difference in daily AOV between groups. Fail to reject the null hypothesis. 
* If p-value < 0.05: There is a statistically significant difference in daily AOV between groups. Reject the null hypothesis.
```

With `scipy` `stats` already imported, we can run the `mannwhitneyu` algorithm on our data, then compare the returned p-value to our initial significance level.

**<u>Inputs of mannwhitneyu:</u>**  
--`control["AOV"]`  
--`test["AOV"]`  
--`alternative`: *two-sided* since we are looking at the difference between the control and test AOV.

```python
u_stat, u_pvalue = stats.mannwhitneyu(
    test["AOV"], control["AOV"], alternative="two-sided"
)

print(f"U-statistic: {u_stat:.4f}")
print(f"p-value: {u_pvalue:.4f}")

>> U-statistic: 508.0000
>> p-value: 0.2717
```

The returned p-value for the Mann-Whitney U test is greater than our significance level, thus, we fail to reject the null hypothesis.

Based on the 30-day trial, there is no statistically significant difference in AOV across the two groups.

___

# Analyzing The Results <a name="Z-test-results"></a>

Through the **Z-Test of Proportions**, we calculated:

```
p-value [0.0000] < significance level [0.05]
```

Thus, we reject the null hypothesis in favor of the alternate - indicating that there is a true relationship between the new UI and the increase in conversion rate, and that the observed relative lift was not due to chance.

<br>

Through the **Mann-Whitney U test** used to assess the statistical impact the new UI had on AOV, we determined the following:

```
p-value [0.2717] > significance level [0.05]
```

Thus, we fail to reject the null hypothesis - indicating that the new UI led to no statistically significant impact on AOV.

<br>

**<u>Conclusion:</u>** We can statistically conclude that the new UI led to more items purchased while not negatively impacting AOV. 

___

# Discussion <a name="discussion"></a>

Our 30-day A/B experiment confirms that the redesigned checkout UI delivered a statistically significant boost in conversion rate without degrading customer average order values.

Cart-to-purchase conversion increased from 40.21% (Control) to 59.13% (Test), representing a +47.03% relative lift in checkout efficiency. While raw AOV showed a slight increase of $0.51 cents per order, non-parametric testing confirmed this difference is not statistically significant with a p-value of 0.2717.

**<u>Business Impact:</u>** These statistical conclusions support the business decision to roll out the redesigned UI to all customers. With the split-testing routing infrastructure already in place, the engineering effort to fully deploy the UI is minimal and carries negligible risk.

**<u>Next Steps:</u>**  
* **Monitor Long-Term AOV Trends Post-Rollout:** Higher cart conversion in theory lays the groundwork for revenue growth over time. We recommend tracking AOV and total revenue across a 60–90 day post-launch window to evaluate whether increased purchase frequency translates into higher revenue.
* **Analyze Behavioral Flow Features for Website-wide Applicability:** Analyze the new UI features (such as simplified fields, button placements, color schemes, widgets, etc) to determine which design features drove the highest lift. Then, identify ways to apply these effective design choices to other areas of the website.
