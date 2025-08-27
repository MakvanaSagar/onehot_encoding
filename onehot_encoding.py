
#IMPORT ALL NEEDED LIBRARY
from sklearn.preprocessing import LabelEncoder
import pandas as pd


#LOAD DATASET
df = pd.read_csv("city.csv")
print("Original Dataset...")
print(df)


#COPY METHOD USED TO - SAFE MY ORIGINAL TABLE
df_label = df.copy()


#ONE-HOT ENCODED PORTION
df_encoded = pd.get_dummies(df, columns=["city"])
print("\n Label Encoded Dataset...")
print(df_encoded.head())