#%%
import pandas as pd
import json
import requests
import os

#%%
dataframes = []
folderPath = "/content/"

csv_files = [f for f in os.listdir(folderPath) if f.endswith(".csv")]

#%%
for file in csv_files:
    filePath = os.path.join(folderPath, file)
    df = pd.read_csv(filePath)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

#%%
combined_df.to_csv("BigWeather.csv")