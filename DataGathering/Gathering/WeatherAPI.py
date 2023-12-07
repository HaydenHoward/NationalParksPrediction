# %%
import pandas as pd
import json
import requests
import os
#%%
NatParkLoc = pd.read_csv("NationalParksLatLong.csv")

for index, row in NatParkLoc.iterrows():

    lat = row['latitude']
    long = row["longitude"]
    response = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2MDEW,T2MWET,T2M_MAX,T2M_MIN,ALLSKY_SFC_LW_DWN,T2M,PRECTOTCORR,WS2M,WS2M_MAX,WS2M_MIN,GWETTOP&community=AG&longitude={long}&latitude={lat}8&format=json&start=2012&end=2022")
    
    if response.status_code == 200:
        data = response.json()["properties"]["parameter"]
        data_1 = response.json()["geometry"]["coordinates"]
        df = pd.DataFrame(data)
        df["yearMonth"] = df.index
        df['year'] = df['yearMonth'].str[:4]
        df['month'] = df['yearMonth'].str[4:]
        df = df.reset_index(drop=True)
        df["latitude"] = data_1[1]
        df["longitude"] = data_1[0]
        df["elevation"] = data_1[2]

        df.to_csv(f"NationalWeather/ParksWeather{index}.csv",index=False)


#%%
# NatParkLoc = pd.read_csv("NationalParksLatLong.csv")

# for index, row in NatParkLoc.iterrows():

lat = 37.585866
long = -85.673305
response = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2MDEW,T2MWET,T2M_MAX,T2M_MIN,ALLSKY_SFC_LW_DWN,T2M,PRECTOTCORR,WS2M,WS2M_MAX,WS2M_MIN,GWETTOP&community=AG&longitude={long}&latitude={lat}8&format=json&start=2012&end=2022")

if response.status_code == 200:
    data = response.json()["properties"]["parameter"]
    data_1 = response.json()["geometry"]["coordinates"]
    df = pd.DataFrame(data)
    df1 = pd.DataFrame(data_1)
    # df["yearMonth"] = df.index
    # df['year'] = df['yearMonth'].str[:4]
    # df['month'] = df['yearMonth'].str[4:]
    # df = df.reset_index(drop=True)
    # df["latitude"] = data_1[1]
    # df["longitude"] = data_1[0]
    # df["elevation"] = data_1[2]

    # df.to_csv(f"dataTryMe.csv",index=False)
# %%
