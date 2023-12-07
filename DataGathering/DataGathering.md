## Introduction

## Data

* NationalParksLatLong.csv - Using the National Parks API the latitude, Longitude, and other data was retrieved. 

* ParksWeather[i].csv - A series of weather data based on the latitude and longitude from national parks the NASA API was used to gather the data. 

* BigWeather.csv - The combination of the individual weather files from the NationWeather folder.

## Data Dictionary 
* **Park Unit**: The name of the Park, Site, or Area
* **Total Recreation Visits**: Total Recreation Visits
* **Total Visitor Spending**: Total Visitor Spending
* **Jobs**: Total Jobs Contributed
* **Labor Income**: Total Labor Income Contributed
* **Value Added**: Total Value Added Contributed
* **Economic Output**: Total Economic Output Contributed
* **latitude**: Latitude of the city
* **longitude**: Longitude of the city
* **city**: City located in or near the park where the weather data is collected.
* **postal**: The postal or zip code of the city
* **T2M**: The average air (dry bulb) temperature at 2 meters above the surface of the earth
* **WS2M**: The average of wind speed at 2 meters above the surface of the earth
* **T2MDEW**: The dew/frost point temperature at 2 meters above the surface of the earth.
* **T2MWET**: The adiabatic saturation temperature which can be measured by a thermometer covered in a water-soaked cloth over which air is passed at 2 meters above the surface of the earth.
* **GWETTOP**: The percent of soil moisture a value of 0 indicates a completely water-free soil and a value of 1 indicates a completely saturated soil; where surface is the layer from the surface 0 cm to 5 cm below grade.
* **T2M_MAX**: The maximum hourly air (dry bulb) temperature at 2 meters above the surface of the earth in the period of interest
* **T2M_MIN**: The minimum hourly air (dry bulb) temperature at 2 meters above the surface of the earth in the period of interest.
* **WS2M_MAX**: The maximum hourly wind speed at 2 meters above the surface of the earth.
* **WS2M_MIN**: The minimum hourly wind speed at 2 meters above the surface of the earth
* **PRECTOTCORR**: The bias corrected average of total precipitation at the surface of the earth in water mass (includes water content in snow). 
* **ALLSKY_SFC_LW_DWN**: The downward thermal infrared irradiance under all sky conditions reaching a horizontal plane the surface of the earth. Also known as Horizontal Infrared Radiation Intensity from Sky.
* **year**: The year the data was collected
* **month**: The months displayed as values 1-12 corresponding to January to December. 13 as the month value signifies the row as the annual, it is the average, max, min etc. depending on the column.   
* **elevation**: The custom site elevation in meters to produce the corrected atmospheric pressure adjusted for elevation.



## Resources
[GeeksforGeeks](https://www.geeksforgeeks.org/how-to-scrape-all-pdf-files-in-a-website/)

[National Parks Stats Map](https://irma.nps.gov/Stats/)

[National Parks Quick Search](https://irma.nps.gov/DataStore/Search/Quick)

[National Parks 2022 Visitor Spending Effects](https://www.nps.gov/subjects/socialscience/vse.htm)

[How to Scrape and Extract Data from PDFs Using Python and tabula-py](https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-fe2dc96b1e68)

[Best U.S. National Parks for 2023](https://travel.usnews.com/rankings/best-national-parks-in-the-usa/)

[National Parks API](https://www.nps.gov/subjects/digital/nps-data-api.htm)

[NASA API](https://power.larc.nasa.gov/data-access-viewer/)