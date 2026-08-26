import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\DS with Amit sir\\second_data\\retail_marketing_sales.csv")

df.head()

df.info()
# datatype object(2),int64(3) and float64(2)

df.isnull().sum() # no null values in dataset

df.describe().sum() # 150 entries and total 7 colums


print(df.duplicated())


"""
Store_Area_sqft          12264.047859
Marketing_Spend_Lakhs      183.604704
No_of_Promotions           192.052197
Avg_Footfall_per_Day      2587.957099
Monthly_Sales_Lakhs        303.363829


       Store_Area_sqft  Marketing_Spend_Lakhs  No_of_Promotions  Avg_Footfall_per_Day  Monthly_Sales_Lakhs
count       150.000000             150.000000        150.000000            150.000000           150.000000
mean       1907.753333               5.104600          6.406667            374.406667            23.205867
std         657.294525               2.857604          3.645530            164.300433            10.607962
min         814.000000               0.600000          1.000000             80.000000             3.000000
25%        1344.500000               2.582500          3.000000            241.000000            14.475000
50%        1878.000000               4.875000          6.000000            360.000000            22.730000
75%        2514.500000               7.655000         10.000000            507.250000            32.215000
max        2998.000000               9.930000         12.000000            711.000000            47.130000

"""

# plt.hist(df['Marketing_Spend_Lakhs'],bins=100)


city_summary = df.groupby('City').agg(
    Total_Stores = ('Store_ID','count'),
    Avg_area_sqft = ('Store_Area_sqft','mean'),
    Total_Sales_Lakhs = ('Monthly_Sales_Lakhs','sum'),
    Avg_Monthly_sales = ('Monthly_Sales_Lakhs','mean'),
    # Fixed the typo here: Speed -> Spend
    Avg_Marketing_Spend_lakhs = ('Marketing_Spend_Lakhs','mean'), 
    Avg_Footfall_per_day = ('Avg_Footfall_per_Day','mean')
).reset_index()

print(city_summary.to_string(index=False))

