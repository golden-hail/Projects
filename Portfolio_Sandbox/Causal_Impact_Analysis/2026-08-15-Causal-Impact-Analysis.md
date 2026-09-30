---
layout: post
title: Quantifying Sales Uplift With Causal Impact Analysis
image: "/posts/checkout_UI.jpg"
tags: [Causal Impact Analysis, Python]
---

Our grocery retailing client is back with another request! The client is interested in understanding how  campaign has affected shopper's daily spending

Causal Impact Analysis will be used in order to see these effects.

---link to first post?
___

# Table of Contents

- [00. Project Overview](#overview-main)
    - [Context](#overview-context)
    - [Actions](#overview-actions)
    - [Results & Discussion](#overview-results)
- [01. Concept Overview](#concept-overview)
- [02. Data Overview & Preparation](#data-overview)
- [03. Applying Causal Impact Analysis](#causal-impact)
- [04. Analyzing The Results](#results)
- [05. Discussion](#discussion)


___

# Project Overview  <a name="overview-main"></a>
<br>
### Context <a name="overview-context"></a>

In late June, a grocery retailer ran a campaign to promote their new “Delivery Club” memberships. Signing up for the club costs $100 and gives customers free grocery deliveries for one year, starting July 1st.

This retail client is now curious if customers who signed up for the Delivery Club have increased their spending in the months following the membership launch date. 

~For now, we'd just really like to understand the uplift in sales for customers that joined the club, over and above what they would have spent had the club not come into existence.~

<br>

### Actions <a name="overview-actions"></a>

To do this, we'll be using ... to find uplift in sales? 

understanding and measuring a key business metric after some event has taken place. 

measuring change with a time series analysis approach 

counterfactual prediction 

The *campaign_data* table include data from the Delivery Club campaign, such as which mailer was sent, if they signup, etc. (who was mailed each type of mailer asnd if they signed up.)

but we know that since the membership was open to EVERYONE so our control group doesn't really represent a clea ngroup of custoemrs

The *control* group could instead be used to measure the impact we had from contacting customers, but abc want to know the overall impact on sales of the membership itself.

find the average daily sales for customers who signed up for the membership and use those customers who did not sign up as our control group...

people who didn't sign up *should* continue their normal shopping habits after the embership went live on July 1st, which will help us create the counterfactual for those customers who DID sign up because in theory they should start spending more (and shopping more frequently) due to the free deliveries they are now entitled to

blurb on Google causal impact?

calculate uplift of who signed up 

In short, Causal Impact analysis predicts what would have happened if an event never took place, and compares that prediction to what actually happened.

<br>

### Results & Discussion <a name="overview-results"></a>

Executive Summary: Include a 1-page summary explaining the model findings in terms of business impact (e.g., "Increasing tenure by 12 months reduces churn odds by 34% according to Logistic Regression").

???Our hypothesis was that if customers are not paying for deliveries, they'll be tempted to shop with us more frequently, and hopefully even purchase more each time.???

___

# Concept Overview 
<br>

.It is a statistical method (and an open-source code package) built by researchers at Google back in 2014. It is heavily used in data science, econometrics, and digital marketing to figure out the actual impact of an event when you can't run a standard A/B test.What is it, exactly?In short, Causal Impact analysis predicts what would have happened if an event never took place, and compares that prediction to what actually happened.Imagine you run an e-commerce store and launch a massive TV ad campaign on June 1st. Sales go up 20% over the next two weeks. Was it the TV ad? Or was it just a normal seasonal surge, organic growth, or a competitor dropping out?Since you can't split the entire country into a randomized control group for a TV ad, Causal Impact solves this by creating a counterfactual baseline (a synthetic control group).  How the Magic WorksFind Unaffected Controls: You give the algorithm metrics that aren't affected by your event (e.g., competitors' search volume, web traffic in a region where the ad didn't air, or historical market trends).Train the Model: The algorithm looks at the historical relationship between your target metric (your sales) and those control metrics before the event took place.  Predict the Counterfactual: It uses those control metrics to forecast what your sales should have looked like after June 1st if the TV ad never existed.Calculate the Lift: The gap between your actual sales and the predicted sales is the "causal impact" of your decision.  Metric Value
       ^
       |              Actual Performance (With Event)
       |                   /---------\
       |                  /  CAUSAL   \
       |      Event      /   IMPACT    \
       |        |       /   (The Gap)   \
       |        v      /.................\  Predicted Counterfactual
       |--------------*                   * (What would have happened)
       |             / \................./
       |____________/
       +--------------------------------------------> Time
                 Pre-Period         Post-Period

No A/B Test Required: It handles real-world scenarios where traditional A/B testing is impossible, unethical, or too expensive.

Handles Complexity: It accounts for trends, seasonality (e.g., weekends vs. weekdays), and historical patterns automatically using Bayesian structural time-series models.  

why it is good:

Why your teacher is hyped about itEven though it's over a decade old, it remains a gold standard in industry because:No A/B Test Required: It handles real-world scenarios where traditional A/B testing is impossible, unethical, or too expensive.Handles Complexity: It accounts for trends, seasonality (e.g., weekends vs. weekdays), and historical patterns automatically using Bayesian structural time-series models.  Quantifies Uncertainty: Instead of giving you a single flat guess, it gives you confidence intervals (e.g., "We are 95% confident the campaign generated between +12% and +18% revenue lift"). 

To prepare the data for the CausalImpact function, the final DataFrame must be uniquely indexed by a continuous date timeline. The function requires:A Target Variable (Column 1): The metric we want to evaluate (the treatment group).Control Variables (Remaining Columns): Unaffected time-series used to predict the counterfactual baseline.For this analysis, we will calculate the mean daily spend across our two distinct shopper segments: members who signed up for the Delivery Club campaign (the treatment group) and members who did not (the control group). Each column will represent a group's average daily spend, aligned sequentially by a common date index.
___

# Data Overview & Preparation  <a name="data-overview"></a>
<br>

First, import the required packages for data processing and casual impact analysis:

```python
from causalimpact import CausalImpact
import pandas as pd
```

Next, we'll import and merge our data tables of interest:

* The *transactions* table contains individual customer transactions, with fields such as ***date of purchase, total_cost, total_items***

* The *campaign_data* table contains data from the Delivery Club campaign, tracking which type of mailer each customer received and whether they signed up or not.

```python
# Import data tables
transactions = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'transactions')
campaign_data = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'campaign_data')
```

Because the *transactions* table tracks data from April through September, daily sales serves as the appropriate time-series metric. We group the data by `customer_id` and `transaction_date` to aggregate individual daily spending into a new DataFrame: customer_daily_sales. Retaining customer_id at this stage allows us to successfully merge the aggregated sales numbers with our *campaign_data* table.


```python
# Aggregate sales cost per customer per day
customer_daily_sales = transactions.groupby(['customer_id', 'transaction_date'])['sales_cost'].sum().reset_index()

# Merge data tables on customer_id
customer_daily_sales = pd.merge(customer_daily_sales, campaign_data, how = 'inner', on = 'customer_id')
```

!!! Start here 

To prepare the DataFrame input for the `CausalImpact` function, we'll want to further refine our DataFrame to be uniquely indexed by daytime series data. For the columns in this table, we'll want the mean daily spent for both groups, the members who did and the members who didn't sign up.

We want the average / mean spent per day for all the customers -  provided the columns are aligned by a common time index

Required Columns: One target variable column (the metric you want to evaluate) and one or more control variable columns (unaffected series used to predict the counterfactual baseline).

 Each row with a date entry will include the average spent per day by shoppers in the categories of people who did and didn't sign up for the delivery club campaing. Each column will represent whether a customer signed up or didn't sign up

```python
causal_impact_df = customer_daily_sales.pivot_table(index =                 'transaction_date',
                                                    columns = 'signup_flag',
                                                    values = 'sales_cost',
                                                    aggfunc = 'mean')

```

***insert sample data*** 0 = didn't sign up averages and 1 = signed up averages****

Clean up our data a bit further for the analysis:

```python
# Provide a frequency for our DateTimeIndex ("D" = daily) 
causal_impact_df.index.freq = "D"

# for causal impact we need the impacted group in the first column (see required columns)
causal_impact_df = causal_impact_df[[1,0]]

# Rename columns
causal_impact_df.columns = ["member", "non_member"]
```
___

# Applying Causal Impact Analysis <a name="z-test-application"></a>

From here, we are curious as to how customer daily spending changed -

In short, Causal Impact analysis predicts what would have happened if an event never took place, and compares that prediction to what actually happened. 

Inputs?

The pre_period for this data is for data before the grocery Club membership began.

The post_period is the period after the Delivery Club memberships started

```python
pre_period = ["2020-04-01","2020-06-30"]
post_period = ["2020-07-01","2020-09-30"]

ci = CausalImpact(causal_impact_df, pre_period, post_period)
```

From here, our causal_impact object??? has been created. there are many methods that could be used for analysis but we only need the plot and summary for our purposes 

<br>
___

# Analyzing The Results <a name="Z-test-results"></a>

PLot and explain the impact... predicted counterfactual with confidence thresholds.

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

method, Scale: If you have multiple years of daily data across thousands of parallel control markets, standard execution will crawl. Because it runs on TensorFlow, tfcausalimpact handles deep computations much faster if we had mroe data...

mention tensor Flow option for larger data sets 

Ensure pip install tfcausalimpact for Tensor Flow, avoid warnings.. .won't be in the anaconda .. . translates your DataFrame into a format built for TensorFlow Probability (tfp.sts)