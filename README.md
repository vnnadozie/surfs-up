# surfs-up
![image](https://user-images.githubusercontent.com/111776924/201540819-241ea7f4-4f07-4242-a257-e621a679ba88.png)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. 

Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.Use SQLAlchemy create_engine to connect to your sqlite database.Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
Precipitation Analysis

Design a query to retrieve the last 12 months of precipitation data.Select only the date and prcp values.Load the query results into a Pandas DataFrame and set the index to the date column.Sort the DataFrame values by date.Plot the results using the DataFrame plot method.
