# STATS MODULE OF SCIPY
# import 2 modules from scipy library contains useful mathematical functionality. useful statistical concepts and tools
# chi2_contingency module: chi squared statistic and p value (when we instantiate it, define it?)
# chi2 module: allows us to find the critical value based on our acceptance criteria 

# IMPORT REQUIRED PACKAGES
import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Then we'll import our data

# IMPORT DATA
campaign_data = pd.read_excel('grocery_db.xlsx', sheet_name = "campaign_data")

# FILTER OUR DATA
campaign_data = campaign_data.loc[campaign_data['mailer_type'] != 'Control']

# now we'll create the 2x2 matrix needed for the chi2 approach , using a method called crosstab

## !!! insert picture of chisquare test of independence ??

observed_vals = pd.crosstab(campaign_data['mailer_type'],campaign_data['signup_flag'])

'''
>>> signup_flag    0    1
>>> mailer_type          
>>> Mailer1      252  123
>>> Mailer2      209  127
'''

# our chi-squared contingincy function requires the input to be an array, so we specify we want *.values()* at the end of our statement

observed_vals = pd.crosstab(campaign_data['mailer_type'],campaign_data['signup_flag'])
print(observed_vals)
'''
>>> array([[252, 123],
       [209, 127]])
'''

# manually calculate what the sign-up rates were for each customer who received a mailer 

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)
print(mailer1_signup_rate, mailer2_signup_rate)


