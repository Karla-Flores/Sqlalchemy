<h1>Sqlalchemy--Challenge</h1>
<hr>
<h3>Background</h3>
<hr>
<br>
<p>This assignment involved analysing and exploring Hawaii's climate data in 2 steps:</p>
<ol>
<li>Climate Analysis and Exploration</li>
<li>Climate App</li>
</ol>
<br>
<h3>Climate Analysis and Exploration</h3>
<hr>
<p align= 'justify'>Python and SQLAlchemy was used to do basic climate analysis and data exploration of the given climate database. All of the analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.<p>
<br>
<h4>Precipitation Analysis</h4>
<p align= 'justify'>
<ul>
<li>The datetime library was used to identify the date 12 months prior to the last date available. Using these dates and after dropping null values, the precipitation values for the last year of data was used to plot the following graph:</li>
<br>
<img width="984" alt="Screen Shot 2021-06-29 at 9 49 04 PM" src="https://user-images.githubusercontent.com/77529968/123894471-d543b880-d923-11eb-9839-79d64944d95c.png">
<br>
<li>A statistics summary using .describe() revealed the following:</li>
<br>
<img width="129" alt="Screen Shot 2021-06-29 at 9 53 48 PM" src="https://user-images.githubusercontent.com/77529968/123894836-7df21800-d924-11eb-9fd6-2b8531958523.png">
</p>
<br>
<h4>Station Analysis</h4>
<p align = 'justify'>This section asked to find the number of stations (nine) and the most active station (USC00519281).</p>
<p align = 'justify'>Temperature observations at this station for the last 12 months was plotted as a histogram with the following results:
</p>
<br>
<p align = 'justify'>
<img width="703" alt="Screen Shot 2021-06-29 at 10 02 42 PM" src="https://user-images.githubusercontent.com/77529968/123895630-bc3c0700-d925-11eb-974a-8f63e859c3b9.png"></p>
<br>
<h3>Climate App</h3>
<hr>
<br>
