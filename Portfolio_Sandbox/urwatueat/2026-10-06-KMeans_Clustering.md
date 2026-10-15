---
layout: post
title: Title and image and tag??
image: "/posts/checkout_UI.jpg"
tags: [AB Testing, Hypothesis Testing, Z-Test, Shapiro-Wilk, Mann-Whitney U, Python]
---

We'll be modeling customer groups with KMeans clustering.

A basic exploration into K-Means Clustering

___

# Table of Contents

- [00. Project Overview](#overview-main)
    - [Context](#overview-context)
    - [Actions](#overview-actions)
    - [Results & Discussion](#overview-results)
- [01. Data Overview & Preparation](#data-overview)
- [02. Applying Z-Test for Proportions](#z-test-application)
- [05. Analyzing The Results](#test-results)
- [06. Discussion](#discussion)

___

# Project Overview  <a name="overview-main"></a>
<br>
### Context <a name="overview-context"></a>

In this scenario, a management team is looking to segment their customer database in order to target the segmented groups for effective promotions and sales, specifically in their grocery products. (To be able to use them for, marketing strategies deals and discounts)

Some of the team think that everyone buys from all the food departments, 
just varying amounts depending on how many are in their household. 
Others in the team think there are specific diets or preferences at play, 
meaning that some customers shop or don’t shop in certain product areas 
due to their lifestyles.

~To be able to use them for, marketing strategies deals and discounts

when considering the cost of spend in different product area

To find distinct groups of customers with a data driven approach to find distinct groups of customers or disstinct behaviors 

simple way to target their customers with relevent content and offers 

<br>

### Actions <a name="overview-actions"></a>


<br>

### Results & Discussion <a name="overview-results"></a>



___

# Data Overview & Preparation  <a name="data-overview"></a>
<br>

First, the data must be imported as well as the needed python libraries. Talk about them

```python
# Import required Python packages

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

# import tables
transactions = pd.read_excel("data/grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("data/grocery_database.xlsx", sheet_name = "product_areas")
```

<br>
Below is a 5 row sample of the imported **transactions** DataFrame. This DataFrame contains months transaction data, broken down by purchase date and product area:
<br>

| **customer_id** | **transaction_date** | **transaction_id** | **product_area_id** | **num_items** | **sales_cost** |
| --- | --- | --- | --- | --- | --- |
| 4 | 2020-04-01 00:00:00 | 435561454899 | 4 | 6 | 52.18 |
| 4 | 2020-04-01 00:00:00 | 435561454899 | 3 | 1 | 3.45 |
| 4 | 2020-04-01 00:00:00 | 435561454899 | 5 | 1 | 8.57 |
| 4 | 2020-04-01 00:00:00 | 435561454899 | 1 | 5 | 129.76 |
| 5 | 2020-04-01 00:00:00 | 435561670722 | 4 | 15 | 76.74 |

In the **transactions** DataFrame we have the following columns:

* customer_id (for each purchase, non-unique)
* transaction_date
* transaction_id
* product_area_id (which product area the purchased items were from)
* num_items (number of items bought from that product area)
* sales_cost (of the number of items purchased in that product area)

<br>
The table below contains the data table of the imported **product_areas** DataFrame:
<br>

| **product_area_id** | **product_area_name** | **profit_margin** |
| --- | --- | --- |
| 1 | Non-Food | 0.25 |
| 2 | Vegetables | 0.18 |
| 3 | Fruit | 0.14 |
| 4 | Dairy | 0.19 |
| 5 | Meat | 0.11 |

To get the product area names into the **transactions** DataFrame, the two imported tables are to be merged on the `product_area_id` column. We'll also drop the non-food categories as we are curious as to dietary needs

```python
# merge on product area name
transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

# drop the non-food category
transactions.drop(transactions[transactions["product_area_name"] == "Non-Food"].index, inplace = True)
```

Since we are profiling customers by the product areas they buy from, (does that sound politically correct??) we will want to aggregate our sales data for a transaction summary at this level

```python
# aggregate sales at customer level (by product area)
transaction_summary = transactions.groupby(["customer_id", "product_area_name"])["sales_cost"].sum().reset_index()
```

| **customer_id** | **product_area_name** | **sales_cost** |
| --- | --- | --- |
| 1 | Dairy | 367.74 |
| 1 | Fruit | 276 |
| 1 | Meat | 543.38 |
| 1 | Vegetables | 167.12 |
| 2 | Dairy | 150.63 |

Notice that there are still multiple entries per customer. Since this aanalysis involves segmenting customers, we want a row per customer and product areas as columns.We also want the total spent for each customer. Use a pivot table:

```python
# pivot data to place product areas as columns
transaction_summary_pivot = transactions.pivot_table(index = "customer_id",
                                columns = "product_area_name",
                                values = "sales_cost",
                                aggfunc = "sum",
                                fill_value = 0,
                                margins = True,
                                margins_name = "Total").rename_axis(None, axis = 1)
```

| **customer_id** | **Dairy** | **Fruit** | **Meat** | **Vegetables** | **Total** |
| --- | --- | --- | --- | --- | --- |
| 1 | 367.74 | 276 | 543.38 | 167.12 | 1354.24 |
| 2 | 150.63 | 120.93 | 241.21 | 99.05 | 611.82 |
| 3 | 46.2 | 75.39 | 171.13 | 31.5 | 324.22 |
| 4 | 341.91 | 245.36 | 272.79 | 142.35 | 1002.41 |
| 5 | 694.71 | 815.32 | 1405.19 | 350.1 | 3265.32 |

Then get percentages of sales for each product_area for each customer compared to the total sales. Once this calculation is done, we can drop the "Total" column because we don't need it for KMeans Clustering:

```python
# Turn sales into % sales
transaction_summary_pivot = transaction_summary_pivot.div(transaction_summary_pivot["Total"], axis = 0)

# drop the "total" column 
data_for_clustering = transaction_summary_pivot.drop(["Total"], axis = 1)
```

Now taht we are ready for the ML part, we can normalize the data. Before doing so, do a quick check to see if there are missing values. Missing values cause issues for the KMeans algorithm as it has trouble plotting datapoints along dimensions where the data is not present. There isn't. 

Now to scale our data - our percentages we are clustering are already between 0 and 1, however good to normalize

one product area *may* commonly make upa large portion of customer sales and this may end up domincating the clustering space.

If we normalize our data, the product areas that make up smaller portions of volumes will be spread proportionally between 0 and 1 with library XX (why not standarize?)

*** use scaled values when clustering the data but when profiling each cluster, may want to use the actual values

```python
# check for missing values
data_for_clustering.isna().sum()

# normalize data
scale_norm = MinMaxScaler()
data_for_clustering_scaled = pd.DataFrame(scale_norm.fit_transform(data_for_clustering), columns = data_for_clustering.columns)
```

With our data scaled, we are ready (why fit transform above but just but not for k in k_values?)

___

# Applying WCSS to Determine k <a name="z-test-application"></a>

<br>

What value do we want for K? the age old problem. Use Winthin Cluster Sum of Squares or WCSS. What is it? We'll plot the WCSS score against k to see where the elbow bends

Let's create a list of k values we'd like to test:

```python
k_values = list(range(1,10))
wcss_list = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_for_clustering_scaled)
    wcss_list.append(kmeans.inertia_) 

plt.plot(k_values, wcss_list)
plt.title("Within Cluster Sum of Squares - by k")
plt.xlabel("k")
plt.ylabel("WCSS Score")
plt.tight_layout()
plt.show()
```

EMBED PLOT PHOTO

From the plot, we see the elbow around 3 clusters would be good, now run KMeans. 


<br>

___

# Applying KMeans Clustering <a name="test-results"></a>

n_init? instantiate our KMeans model like before but replace k with 3

```python
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(data_for_clustering_scaled)
```

add the cluster labels to the original dataframe before it was scaled to see which cluster each customer fell into. Then let's look at the counts to see how many customers are in each cluster.

```python
# Add cluster labels to our data
data_for_clustering["cluster"] = kmeans.labels_

# check cluster sizes
data_for_clustering["cluster"].value_counts()

'''
1    641
0    127
2    103
'''
```

Lastly, we'll profile our clusters by group together to better understand what these clusters mean.

For each cluster, calculate the mean percentage of sales for each of our product areas 

```python
cluster_summary = data_for_clustering.groupby("cluster")[["Dairy", "Fruit", "Meat", "Vegetables"]].mean().reset_index()
```

| **cluster** | **Dairy** | **Fruit** | **Meat** | **Vegetables** |
| --- | --- | --- | --- | --- |
| 0 | 0.363948 | 0.394152 | 0.0292098 | 0.21269 |
| 1 | 0.220875 | 0.264605 | 0.376508 | 0.138011 |
| 2 | 0.00238212 | 0.637796 | 0.00369612 | 0.356126 |

The cluster summary above 

calculated the mean 

can see the mean percentage that customers within that cluster allcoate to shopping in those product areas.

Customers in cluster 0 allocating on average 3% of their purcahses to the meat category - could be a vegeatrian category

Cluster 1 is pretty uniform across it's means, suggesting that customers are shopping across teh board in that cluster. 

Cluster 2 low meat and dairy so perhaps vegan customers

More meat eater than those 2 combined, less vegatarian and vegan shoppers 

Could make the assumption that groups are vegan and vegetarian (they eat more than that, just the example here, not a ton of data) 

<br>

___

# Analyzing The Results <a name="test-results"></a>

Through the K Means Clustering we were able to segment the database into 3 distinct groups. Our results suggest that the third group of customers containing X people may be vegetarian or something.


**<u>Conclusion:</u>** 

___

# Discussion <a name="discussion"></a>

Understand customer base better and see which trends are coming and going? How this profiling can be used to 

**<u>Business Impact:</u>** 

**<u>Next Steps:</u>**  
* **Monitor Long-Term AOV Trends Post-Rollout:** Higher cart conversion in theory lays the groundwork for revenue growth over time. We recommend tracking AOV and total revenue across a 60–90 day post-launch window to evaluate whether increased purchase frequency translates into higher revenue.
* **Analyze Behavioral Flow Features for Website-wide Applicability:** Analyze the new UI features (such as simplified fields, button placements, color schemes, widgets, etc) to determine which design features drove the highest lift. Then, identify ways to apply these effective design choices to other areas of the website.
