import pandas as pd
from scipy import stats

# Load Data
data = pd.read_csv('../data/insurance_data.csv')

# Hypotheses
province_risk = data.groupby('Province')['TotalClaims'].mean()
gender_risk = data.groupby('Gender')['TotalClaims'].mean()

# T-test for Gender Differences
male_claims = data[data['Gender'] == 'Male']['TotalClaims']
female_claims = data[data['Gender'] == 'Female']['TotalClaims']

t_stat, p_value = stats.ttest_ind(male_claims, female_claims)
print(f"T-test (Male vs Female Claims): p-value = {p_value}")

# Province Analysis
f_stat, p_value_prov = stats.f_oneway(*[group['TotalClaims'].values 
                                        for name, group in data.groupby('Province')])
print(f"ANOVA Test (Across Provinces): p-value = {p_value_prov}")

if p_value < 0.05:
    print("Significant gender difference in claims (Reject Null)")
else:
    print("No significant gender difference (Fail to Reject Null)")

if p_value_prov < 0.05:
    print("Significant claim differences across provinces (Reject Null)")
else:
    print("No significant claim difference across provinces (Fail to Reject Null)")
