
##############################################################################
# AB TESTING - Chi-Squared Test
##############################################################################

# Import required packages - 

import pandas as pd 
from scipy.stats import chi2_contingency, chi2

# Import data - 

campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name = "campaign_data")

# Filtering the data - 

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

# Summarise to get our observed frequencies - 

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values()

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)
print(mailer1_signup_rate, mailer2_signup_rate)

# State hypothesis & set acceptance criteria - 

null_hypothesis = "There is NO replationship between mailer type and sign up rate."
alternate_hypothesis = "There is a replationship between mailer type and sign up rate."
acceptance_criteria = 0.05

# Calculate expected frequencies and chi-square statistic.

chi2_statistic, p_value, dof, expecteed_values = chi2_contingency(observed_values, correction = False) # Correction - False because dof = 1
print(chi2_statistic, p_value)
 
# Find the critical value for our test - 
critical_value = chi2.ppf(1 - acceptance_criteria, dof)

# Print the result (Chi Square Statistic)- 

if chi2_statistic >= critical_value :
    print("As our chi-square statistic is higher than our critical value, we REJECT the null hypothesis.")
else:
    print("As our chi-square statistic is lower than our critical value, we ACCEPT the null hypothesis.")

# Print the result (p-value)- 

if p_value <= acceptance_criteria :
    print("As our p-value is lower than our acceptance criteria, we REJECT the null hypothesis.")
else:
    print("As our p-value is higher than our acceptance criteria, we ACCEPT the null hypothesis.")





