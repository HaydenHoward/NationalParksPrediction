# %%
import pandas as pd
import json
import requests
import os

# %%
api_key = "bhWQ4u2J2bJC8opEU5pnaiSW6W5hPJl4a7bH2EdX"
endpoint = "https://developer.nps.gov/api/v1/parks?limit=1000"

HEADERS = {"X-Api-Key":api_key}

# %%
response = requests.get(endpoint,headers=HEADERS)
response
# %%
data_1 = json.loads(response.text)
# %%
json_formatted_str = json.dumps(data_1, indent=3)
print(json_formatted_str)
# %%
data = response.json()["data"]
# Small dictionary for later
NationalPark = {"Name":[],"latitude":[],"longitude":[],"city":[],"postal":[]}

for i in data:
    address = i["addresses"]
    name = i["fullName"]
    lat = i["latitude"]
    long = i["longitude"]

    for j in address:
        city = j["city"]
        postal = j["postalCode"]

    NationalPark["Name"].append(name)
    NationalPark["latitude"].append(lat)
    NationalPark["longitude"].append(long)
    NationalPark["city"].append(city)
    NationalPark["postal"].append(postal)

# %%
df = pd.DataFrame(NationalPark)
df.head()
# %%
df.to_csv("NationalParksLatLong.csv",index=False)