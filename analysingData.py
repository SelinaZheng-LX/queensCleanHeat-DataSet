#Team Queens
import pandas as pd
import matplotlib.pyplot as plt
import gdown

clean_heat = pd.read_csv("queensCleanHeat-DataSet/clean_heat_dataset.csv")
#extract stats for a particular categorical column
cat_stats = clean_heat.describe(include=['O'])
print("Borough:\n", cat_stats['Borough'])

#Cleaning the data
#check if any values are null
print("Number of dataponts with null entry for each column:\n",clean_heat.isnull().sum())