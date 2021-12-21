# Climate Analysis (Sql-Alchemy, Flask)

![train_gif](https://user-images.githubusercontent.com/77027814/146935439-7ebfd12d-e0e1-43fe-a7da-4bc2d2c2fc9a.gif)

In this analysis, I took data from a sq.lite file containting weather data for 9 different train stations. I parced it using sqlalchemy, python, pandas and various other libraries.

## Precipitation Parcing
- Found the most recent date in the data set. 
- Then using that date, I retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
- Selected only the date and precipitation values.
- Loaded the query results into a Pandas DataFrame and set the index to the date column.
- Sorted the DataFrame values by date.

- Plotted the results using the DataFrame plot method.

![Precipitation_Analysis](https://user-images.githubusercontent.com/77027814/146996642-747b3f14-d9ef-4ea1-a021-b6e342d19dc2.png)

## Station Parcing (Temperature)

- Designed a query to calculate the total number of stations in the dataset.
- Designed a query to find the most active stations (i.e. which stations have the most rows?).
- Listed the stations and observation counts in descending order.
- Found which station id has the highest number of observations?
- Using the most active station id, calculated the lowest, highest, and average temperature.
- Designed a query to retrieve the last 12 months of temperature observation data (Tobs).
- Filtered by the station with the highest number of observations.
- Queried the last 12 months of temperature observation data for this station.

- Plotted the results as a histogram with bins=12

![Temperature_analysis](https://user-images.githubusercontent.com/77027814/146997996-d523981f-2c86-4ed0-86ad-41170acd039d.png)

## Climate App

I took that information and created a flask api based on my queries. This can be found in ___"app.py"___ file

## Analysis

- Most of the temperatures at station 'USC00519281' over the course of on year were between 73 and 77 degrees 
Because this was a query based off of the station with the most information, this is likely the most accurate and consistent temperature. Therefore, I would advise to use this station. 

- Overall, precipitation is pretty low for most of the year aside from a few peaks in the data set. The data is dispersed, evenly with a STDEV of .47 inches, but the average amount of percipitation is 0.18 inches. So Honolulu, Hawaii would be be a great place to go overall, espesially toward the end of the summer. 

## References:

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1
