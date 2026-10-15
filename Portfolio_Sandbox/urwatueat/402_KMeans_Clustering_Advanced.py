'''
Hello aspiring Data Scientists,

We’ve been really impressed with your work so far, it’s made a huge impact! 
We have another task that we’re not sure how to solve, and we figured you 
might be able to help!

Our Senior Management Team can’t quite agree on how to think about the 
different types of grocery customers that are shopping with us. 
Some of the team think that everyone buys from all the food departments, 
just varying amounts depending on how many are in their household. 
Others in the team think there are specific diets or preferences at play, 
meaning that some customers shop or don’t shop in certain product areas 
due to their lifestyles.

We don’t really know how to tackle this problem - 
but since you’re the data experts, would you be able to look 
through the data, and if possible, try to “segment” up the customers 
based on any differences you find?  

If there are different groups within the customer base, 
please report back and we can discuss how we might go about 
using these insights in practice. We’d be really excited to understand 
these so we can serve us customers in a more targeted way!
'''

##################################################
# K Means Clustering - Advanced Template
##################################################

# Import required Python packages
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

##################################################
# Create the data
##################################################

# import tables
transactions = pd.read_excel("data/grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("data/grocery_database.xlsx", sheet_name = "product_areas")

# merge on product area name
transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

# drop the non-food category
transactions.drop(transactions[transactions["product_area_name"] == "Non-Food"].index, inplace = True)

# aggregate sales at customer level (by product area)
transaction_summary = transactions.groupby(["customer_id", "product_area_name"])["sales_cost"].sum().reset_index()

# pivot data to place product areas as columns
transaction_summary_pivot = transactions.pivot_table(index = "customer_id",
                                columns = "product_area_name",
                                values = "sales_cost",
                                aggfunc = "sum",
                                fill_value = 0,
                                margins = True,
                                margins_name = "Total").rename_axis(None, axis = 1)

# Turn sales into % sales

transaction_summary_pivot = transaction_summary_pivot.div(transaction_summary_pivot["Total"], axis = 0)

# drop the "total" column 

data_for_clustering = transaction_summary_pivot.drop(["Total"], axis = 1)

##################################################
# Data Preparation & Cleaning
##################################################

# check for missing values

print(data_for_clustering.isna().sum())

# normalize data

scale_norm = MinMaxScaler()
data_for_clustering_scaled = pd.DataFrame(scale_norm.fit_transform(data_for_clustering), columns = data_for_clustering.columns)

##################################################
# Use WCSS to find a good value for k
##################################################

k_values = list(range(1,10))
wcss_list = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data_for_clustering_scaled)
    wcss_list.append(kmeans.inertia_) 
    
plt.plot(k_values, wcss_list)
plt.title("Within Cluster Sum of Squares - by k")
plt.xlabel("k")
plt.ylabel("WCSS Score")
plt.tight_layout()
plt.show()
    
##################################################
# Instantiate & fit model
##################################################

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(data_for_clustering_scaled)

##################################################
# Use cluster information
##################################################

# Add cluster labels to our data
data_for_clustering["cluster"] = kmeans.labels_

# check cluster sizes
custs_per_cluster = data_for_clustering["cluster"].value_counts()

cust_count_percentage = round(data_for_clustering["cluster"].value_counts() / data_for_clustering["cluster"].value_counts().sum()*100, 2)

data_for_clustering["% of custs in cluster"] = data_for_clustering["custs in cluster"] / data_for_clustering["custs in cluster"].sum()

##################################################
# Profile our Clusters
##################################################

cluster_summary = data_for_clustering.groupby("cluster")[["Dairy", "Fruit", "Meat", "Vegetables"]].mean().reset_index()

percent_cols = cluster_summary.columns.tolist()[1:5]

cluster_summary[percent_cols] = round(cluster_summary[percent_cols]*100, 2)

# append customers per cluster and customer percentage per cluster
cluster_summary['# of customers'] = custs_per_cluster
cluster_summary['% of customers'] = cust_count_percentage

