################################################################
# Causal Impact Analysis
################################################################

'''
Hello aspiring Data Scientists,

As you know from previous projects, in July, we sent out mailers in a marketing campaign for our "delivery club". This was a new initiative that cost customers $100 per year for membership, and offered free grocery deliveries rather than the normal cost of $10 per delivery.

We really want to understand if customers who joined the club have increased their spending with us in the months following. Our hypothesis was that if customers are not paying for deliveries, they'll be tempted to shop with us more frequently, and hopefully even purchase more each time.

For now, we'd just really like to understand the uplift in sales for customers that joined the club, over and above what they would have spent had the club not come into existence - is this something you could help us with?

As always, we appreciate your hard work,
ABC Grocery Marketing Team
'''

################################################################
# Import required packages
################################################################

from causalimpact import CausalImpact
import pandas as pd

################################################################
# Import & create data
################################################################

# Import data tables

transactions = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'transactions')
campaign_data = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'campaign_data')

# Aggregate transactions data to customer, date level

customer_daily_sales = transactions.groupby(['customer_id', 'transaction_date'])['sales_cost'].sum().reset_index()

# Merge on the signup flag

customer_daily_sales = pd.merge(customer_daily_sales, campaign_data, how = 'inner', on = 'customer_id')


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

################################################################
# Apply Causal Impact
################################################################

pre_period = ["2020-04-01","2020-06-30"]
post_period = ["2020-07-01","2020-09-30"]

ci = CausalImpact(causal_impact_df, pre_period, post_period)

################################################################
# Plot the impact
################################################################

ci.plot()

# Looks like customers who signed up ended up spending more in store!

################################################################
# Extract the summary statistics & report
################################################################

print(ci.summary())
print(ci.summary(output = "report"))


