# %%
from bs4 import BeautifulSoup as bs
import re
import plotly.express as px
import requests
import pandas as pd
from io import StringIO

# %%
site = requests.get("https://en.wikipedia.org/wiki/List_of_areas_in_the_United_States_National_Park_System")

#%%
soup = bs(site.text, "html.parser")

#%%
print(soup.prettify())
# %%

table_html = soup.find_all("table", class_="sortable wikitable")
# table_html = soup.find_all(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="locationTable")

# %%
print(table_html)
# %%
table_to_extract = 0
df = pd.read_html(StringIO(str(table_html[table_to_extract])))[0]
# %%
combined_df = df = pd.read_html(StringIO(str(table_html[0])))[0]

combined_df.head()
#%%
for i in range(24):
    # print(i)
    table_to_extract = i+1
    df = pd.read_html(StringIO(str(table_html[table_to_extract])))[0]
    # print(df)
    # df = df.rename(columns=lambda x: 'Area' if 'Area' in x else x)
    # has_area_column = df.columns.str.contains('Area').any()
    # print(has_area_column)
    # if has_area_column:
    # # Create a dictionary to map old column names to new ones
    #     column_mapping = {col: 'Area' if 'Area' in col else col for col in df.columns}
    #     print(column_mapping)
    # # Rename columns using the dictionary
    #     df = df.rename(columns="Area")
    # combined_df.join(df, on="Name")
    # combined_df = combined_df.join(df.set_index("Name"), on="Name", rsuffix='_new')
    # combined_df = pd.concat(combined_df, df)
    dfs = [df, combined_df]
    combined_df = pd.concat([df.rename(columns=lambda x: 'Area' if 'Area' in x else x) for df in dfs], ignore_index=True)



#%%
# df.head()
# combined_df.head()
combined_df = combined_df.dropna(subset=["Area","Name"])
combined_df = combined_df.drop(columns=["Name[2]","Law","Status","Established","Disbanded","Result","Year established"])
combined_df['Area'] = combined_df['Area'].str.extract(r'([0-9,]+\.[0-9]+) acres')
combined_df['Area'] = combined_df['Area'].str.replace(',', '').astype(float)


# %%
combined_df
combined_df.to_csv("ParkSize.csv",index=False)

# %%
