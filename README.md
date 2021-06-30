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
<h3>Bonus Challenges</h3>
<hr>
