---
layout: post
title: Quantifying Sales Uplift With Causal Impact Analysis
image: "/posts/checkout_UI.jpg"
tags: [Causal Impact Analysis, Python]
---

The grocery company is back and they're inteerested in knowning how the grocery_club campaign has affected shopper's daily spending

To do this, we will be running a causal analysis.

---link to first post?
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

Hello aspiring Data Scientists,

As you know from previous projects, in July, we sent out mailers in a marketing campaign for our "delivery club". This was a new initiative that cost customers $100 per year for membership, and offered free grocery deliveries rather than the normal cost of $10 per delivery.

We really want to understand if customers who joined the club have increased their spending with us in the months following. Our hypothesis was that if customers are not paying for deliveries, they'll be tempted to shop with us more frequently, and hopefully even purchase more each time.

For now, we'd just really like to understand the uplift in sales for customers that joined the club, over and above what they would have spent had the club not come into existence - is this something you could help us with?

As always, we appreciate your hard work,
ABC Grocery Marketing Team

<br>

### Actions <a name="overview-actions"></a>



<br>

### Results & Discussion <a name="overview-results"></a>

Key Takeaways for Your Portfolio Presentation
	• Highlight Trade-offs: Parametric models (Linear/Logistic Regression) assume explicit relationships and yield interpretable coefficients. Non-parametric models (KNN) make fewer assumptions but require scaling and incur higher memory/computation costs at prediction time.
	• Data Preprocessing Focus: Document how scaling changed KNN performance versus Linear Regression to show strong data engineering fundamentals.
Executive Summary: Include a 1-page summary explaining the model findings in terms of business impact (e.g., "Increasing tenure by 12 months reduces churn odds by 34% according to Logistic Regression").

___

# Data Overview & Preparation  <a name="data-overview"></a>
<br>

First we'll import and merge our data tables of interest:

```python
# Import required packages
from causalimpact import CausalImpact
import pandas as pd

# Import data tables
transactions = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'transactions')
campaign_data = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'campaign_data')

# Aggregate transactions data to customer & transaction date level
customer_daily_sales = transactions.groupby(['customer_id', 'transaction_date'])['sales_cost'].sum().reset_index()

# Merge data tables on customer_id
customer_daily_sales = pd.merge(customer_daily_sales, campaign_data, how = 'inner', on = 'customer_id')
```

```python
# Pivot the data to aggregate daily sales by signup group

causal_impact_df = customer_daily_sales.pivot_table(index = 'transaction_date',
                                                    columns = 'signup_flag',
                                                    values = 'sales_cost',
                                                    aggfunc = 'mean')

# provide a frequency for our DateTimeIndex (avoids a warning message)

causal_impact_df.index.freq = "D"

# for causal impact we need the impacted group in the first column

causal_impact_df = causal_impact_df[[1,0]]

# rename columns to something more meaningful

causal_impact_df.columns = ["member", "non_member"]
```
___

# Applying Causal Impact Analysis <a name="z-test-application"></a>

From here, we are curious as to how customer daily spending changed .. not quite right

The pre_period for this data is for data before the grocery Club membership began.

The post_period is the period after the Delivery Club memberships started

```python
pre_period = ["2020-04-01","2020-06-30"]
post_period = ["2020-07-01","2020-09-30"]

ci = CausalImpact(causal_impact_df, pre_period, post_period)
```

<br>
___

# Analyzing The Results <a name="Z-test-results"></a>

PLot and explain the impact

```python
ci.plot()
```
Looks like customers who signed up ended up spending more daily!

```python
# Extract the summary statistics & report
print(ci.summary())
print(ci.summary(output = "report"))
```

**<u>Conclusion:</u>** 

___

# Discussion <a name="discussion"></a>


**<u>Business Impact:</u>** 

**<u>Next Steps:</u>**  

