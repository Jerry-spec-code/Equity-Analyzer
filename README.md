# Stock-Market-Trend-Analyzer
A Flask web application that saves and updates real-time equity prices for different companies in a MySQL database and graphs important statistical trends using Chart.js.

## Languages/Tools/Frameworks used: 
1. Python
2. SQL
3. HTML
4. Flask
5. Chart.js
6. MySQL

## Key features: 
1. The user specifies a ticker as well as a start and end date. 
2. If the data does not already exist in the database, the daily price data is fetched using yfinance, which is then stored in a MySQL database.  
3. The program retrieves the data and uses HTML and Chart.js to graph the open, high, low, close, and volume price for the specified period.
4. On each graph, the 20-day and 50-day weighted moving averages are shown. 

## Screenshots of Project
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/176934431-46e918a9-3459-411c-8d38-c9573f6e2bc2.png">
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/78711575/176934462-59839bdf-77dc-468e-8298-fb50986fddca.png">
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/78711575/176934489-cb5ca56d-382b-4c6e-90f5-7189593e4ed2.png">
<img width="1438" alt="image" src="https://user-images.githubusercontent.com/78711575/176934511-3e3b2be6-f803-4e82-82fc-7c2e4de9caa5.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/176934536-b1e34d5c-4162-411d-992e-d37bc3550d19.png">
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/78711575/176934557-3a5a956b-3e49-4793-b35f-884be3d415d3.png">


### Installing required pip packages: Run the commands below 

```sh
python3 -m venv venv (Set up the virtual environment)
. venv/bin/activate  (Activate the virtual environment)
pip3 install -r requirements.txt (install the required packages)
```

### How to run this project?  
1. Create a new file `serverInfo.py` in the root directory. 
2. Update the credentials to match the database credentials to store the data. See `exampleServerInfo.py` for database variables 
3. In the project directory, run the following:<br/><br/>
``` python3 app.py ```<br/>

Open http://127.0.0.1:5000/ to view the app in your browser.
