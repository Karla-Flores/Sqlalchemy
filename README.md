<h1>Sqlalchemy--Challenge</h1>
<hr>
<h3>Background</h3>
<br>
<p>This assignment involved analysing and exploring Hawaii's climate data in 2 steps:</p>
<ol>
<li>Climate Analysis and Exploration</li>
<li>Climate App</li>
</ol>
<h3>Climate Analysis and Exploration</h3>
<hr>
<p align= 'justify'>Python and SQLAlchemy was used to do basic climate analysis and data exploration of the given climate database. All of the analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.<p>
<h4>Precipitation Analysis</h4>
<p align= 'justify'>
<ul>
<li>The datetime library was used to identify the date 12 months prior to the last date available. Using these dates and after dropping null values, the precipitation values for the last year of data was used to plot the following graph:</li></p>
<br>
<img width="984" alt="Screen Shot 2021-06-29 at 9 49 04 PM" src="https://user-images.githubusercontent.com/77529968/123894471-d543b880-d923-11eb-9839-79d64944d95c.png">
<br>
<li>A statistics summary using .describe() revealed the following:</li>
</ul>
<br>
<p align= 'center'>
<img width="129" alt="Screen Shot 2021-06-29 at 9 53 48 PM" src="https://user-images.githubusercontent.com/77529968/123894836-7df21800-d924-11eb-9fd6-2b8531958523.png"></p>
</p>
<h4>Station Analysis</h4>
<p align = 'justify'>This section asked to find the number of stations (nine) and the most active station (USC00519281).</p>
<p align = 'justify'>Temperature observations at this station for the last 12 months was plotted as a histogram with the following results:
</p>
<br>
<p align = 'center'>
<img width="703" alt="Screen Shot 2021-06-29 at 10 02 42 PM" src="https://user-images.githubusercontent.com/77529968/123895630-bc3c0700-d925-11eb-974a-8f63e859c3b9.png">
</p>
<br>
<h3>Climate App</h3>
<hr>
<br>
<p align = 'justify'>This is a web app in the app.py file, created using SQLAlchemy and Flask API. The climate database can be queried for the following to receive information in JSON format:</p>
<ul>
  <li><b>Precipitation (/api/v1.0/precipitation)</b>: This route displays every date and temperature observation across all weather stations in Hawaii.</li>
  <li><b>Stations (/api/v1.0/stations)</b>: This route displays a list of all 9 stations (ID, Station and Name).</li>
  <li><b>Temperature Observations (/api/v1.0/tobs)</b>: This route displays every date and temperature observation for the most active station in Hawaii (USC00519281) in the last 12 months of data available.</li>
  <li><b>Daily Normals from start date (/api/v1.0/start_date)</b>: This route allows you to enter a start date in the format 'YYYY-MM-DD' to retrieve daily normals (TMIN, TAVG, TMAX) from that date onward until the end of data available.</li>
  <li><b>Daily Normals between start and end date (/api/v1.0/start_date/end_date)</b>: This route allows you to enter a start date AND an end date in the format 'YYYY-MM-DD' to retrieve daily normals (TMIN, TAVG, TMAX) for the date range.</li>
</ul>  
<br>
<h3>Bonus Challenge</h3>
<hr>
<h4>Temperature Analysis I</h4>
<p align = 'justify'>June and December temperature observations were retrieved by converting string dates to DateTime objects to filter queries by month.</p>
<p align = 'justify'>The average temperature in June at all stations across all available years in the dataset is 74.94 (F). And the average temperature in June at all stations across all available years in the dataset is 71.04 (F). Thus, the mean temperature difference between June and December is a mere 3.9 degrees Fahrenheit, which is not much different.</p>
<p align = 'justify'> In this analysis, the t-test was paired and showed a low p-value that indicates that the difference is not significant, which means that you can enjoy a temperature over 70 degrees Fahrenheit all year.</p>
<p align = 'justify'> <img width="981" alt="Screen Shot 2021-06-29 at 11 04 16 PM" src="https://user-images.githubusercontent.com/77529968/123900249-5738df00-d92e-11eb-8d86-bfbbc9f63cf4.png"></p>

<h4>Temperature Analysis II</h4>
<p align = 'justify'>This challenge involved using a predefined function that calculated daily normals for a given date range (2018-06-01 to 2018-06-15). The .timedelta() method from the datetime library was also used to determine matching start and end dates from the previous year.</p>
<p align = 'justify'>With the daily normals, the following graph was plotted using tavg, tmin and tmax values:</p>
<p align = 'center'><img width="320" alt="Screen Shot 2021-06-29 at 11 10 42 PM" src="https://user-images.githubusercontent.com/77529968/123900736-3de46280-d92f-11eb-89e4-fd176951b285.png"></p>

<h4>Daily Rainfall Average</h4>
<p align = 'justify'>In this challenge, the first task was to calculate the precipitation for each weather station and display the results and station information. After querying the databases for both tables and checking for null values, the query results were saved in Pandas data frames to make it easier to manipulate data using groupby and merge. The next data frame is the result:</p>
<p align = 'center'><img width="674" alt="Screen Shot 2021-06-29 at 11 11 12 PM" src="https://user-images.githubusercontent.com/77529968/123900772-505e9c00-d92f-11eb-9781-6ddabcd6e95f.png"></p>

<p align = 'justify'>The second part of this challenge involved finding daily normals for each date of our defined trip from 2017-07-01 to 2017-07-14 (using only the month and day to identify historic data with the same dates) and plotting an area plot as below:</p>
<p align = 'center'>
<img width="982" alt="Screen Shot 2021-06-29 at 11 11 50 PM" src="https://user-images.githubusercontent.com/77529968/123900817-64a29900-d92f-11eb-80b1-857ae21236d0.png"></p>

<p align = 'justify'>Trip daily normals dataframe:</p>
<p align = 'center'>
<img width="427" alt="Screen Shot 2021-06-29 at 11 18 53 PM" src="https://user-images.githubusercontent.com/77529968/123901345-60c34680-d930-11eb-8d1b-d701a79006c9.png">
</p>
