###########################################################
# AB Testing - Our Task for ABC Grocery 
###########################################################

## !! Write what the goal of this is, intelligently, for portfolio
'''
Company ABC Grocery has a promo for a "Delivery CLub" they're launching. 
Signing up costs $100, and provides the customer with free groceries 
for one year starting on July 1st

We want to see if a nicer looking mailer would get more customers to sign up.

We selected 3 groups of customers:
    - "mailer1' Customers who received Mailer 1 (received a cheap, basic piece of sign up mail)
    - 'mailer2' Customers who received Mailer 2 (received a fancy colorful piece of sign up mail)
    - 'Control' Customers who were not sent mail (who signed up)?
'''

# IMPORT REQUIRED PACKAGES
import pandas as pd
from scipy.stats import chi2_contingency, chi2

#import matplotlib.plot as plt

# IMPORT DATA
campaign_data = pd.read_excel('grocery_db.xlsx', sheet_name = "campaign_data")

# FILTER OUR DATA
campaign_data = campaign_data.loc[campaign_data['mailer_type'] != 'Control']

# SUMMARIZE TO GET OUR OBSERVED FREQUENCIES
    
observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values
    # .values to get an array, as opposed to a DataFrame with Mailer Type listed
    
''' DataFrame:
    signup_flag    0    1
    mailer_type          
    Mailer1      252  123
    Mailer2      209  127
    
    vs array: 
    array([[252, 123],
           [209, 127]])
    '''
mailer1_signup_rate = 123 / (252 + 123) # signup good for mailer1 / total count Mailer1
mailer2_signup_rate = 127 / (209 + 127) # signup good for mailer2 / total count Mailer2
print(mailer1_signup_rate, mailer2_signup_rate)

# STATE HYPOTHESIS & SET ACCEPTANCE CRITERIA
null_hypothesis = "There is no relationship between mailer type and signup rate. They are independent"
alternate_hypothesis = "There is a relationship between mailer type and signup rate. They are not independent"
acceptance_criteria = 0.05

# CALCULATE EXPECTED FREQUENCIES & CHI SQUARE STATISTIC
chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)
    # correction = Yate's correction, if dof is == 1 [2 x 2] matrix, correction must be False
print(chi2_statistic, p_value) # 1.941, p_value = 0.1635
    # Because P-Value is greater than our acceptance criteria, we retain the null hypothesis

# FIND THE CRITICAL VALUE FOR OUR TEST
    # Let's just show how we can find this out using the critical value for chi^2 test
critical_value = chi2.ppf(1 - acceptance_criteria, dof) # percentage point function
print(critical_value)

# PRINT RESULTS (Chi Squared Statistic)

if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis and conclude that: {null_hypothesis}")

# PRINT THE RESULTS (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p_value statistic of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p_value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis and conclude that: {null_hypothesis}")

# We suggest to the company that the mailing didn't make a difference - we can save on the fanciness. Spending extra money on making nice mail with little to no return
# should be cautious to make conclusions that fancy mail is actually helping people sign up 