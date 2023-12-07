# %%
from bs4 import BeautifulSoup as bs
import re
import plotly.express as px
import requests
import pandas as pd
from io import StringIO

# %%
site = requests.get("https://churchofjesuschristtemples.org/statistics/milestones/")

#%%
soup = bs(site.text, "html.parser")

#%%
print(soup.prettify())
# %%
table_html = soup.find_all("table", class_="statistics small")
# table_html = soup.find_all(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="locationTable")

# %%
print(table_html)
# %%
table_to_extract = 0
df = pd.read_html(StringIO(str(table_html[table_to_extract])))[0]

#%%
df.head()
# %%
def pull_data(page_url, table_to_extract=0):
    site = requests.get(page_url)
    soup = bs(site.text, "html.parser")
    table_html = soup.find_all("table", class_="statistics small")

    table_to_extract = 0
    df = pd.read_html(StringIO(str(table_html[table_to_extract])))[0]
    return df