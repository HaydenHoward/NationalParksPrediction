#%%
import pandas as pd
import json
import requests
import os

#%%
park12 = pd.read_csv("/content/2012_National_Park_Visitor_Spending.csv")
park13 = pd.read_csv("/content/2013_National_Park_Visitor_Spending.csv")
park14 = pd.read_csv("/content/2014_National_Park_Visitor_Spending.csv")
park15 = pd.read_csv("/content/2015_National_Park_Visitor_Spending.csv")
park16 = pd.read_csv("/content/2016_National_Park_Visitor_Spending.csv")
park17 = pd.read_csv("/content/2017_National_Park_Visitor_Spending.csv")
park18 = pd.read_csv("/content/2018_National_Park_Visitor_Spending.csv")
park19 = pd.read_csv("/content/2019_National_Park_Visitor_Spending.csv")
park20 = pd.read_csv("/content/2020_National_Park_Visitor_Spending.csv")
park21 = pd.read_csv("/content/2021_National_Park_Visitor_Spending.csv")
park22 = pd.read_csv("/content/2022_National_Park_Visitor_Spending.csv")
latlong = pd.read_csv("/content/NationalParksLatLong.csv")
bigWeather = pd.read_csv("/content/BigWeather.csv")

#%%
bigWeather["latitude"] = bigWeather["latitude"].apply(lambda x: float(f"{x:.8g}"))
bigWeather["longitude"] = bigWeather["longitude"].apply(lambda x: float(f"{x:.8g}"))

latlong["latitude"] = latlong["latitude"].apply(lambda x: float(f"{x:.8g}"))
latlong["longitude"] = latlong["longitude"].apply(lambda x: float(f"{x:.8g}"))

#%%
NationalWeather = latlong.merge(bigWeather,on=["latitude","longitude"], how="inner")

Total_National_Park = pd.concat([park12,park13,park14,park15,park16,park17,park18,park19,park20,park21,park22], ignore_index=True)

# Need to make the name column in NationalWeather to the park unit column in Total_National_Park_Visitor_Spending