# Stock-Market-Trend-Analyzer
A Flask web application that saves and updates real-time equity prices for different companies in a MySQL database and graphs important statistical trends using Chart.js.

## Languages/Tools/Frameworks used: 
1. Python
2. SQL
3. TypeScript
4. HTML
5. Flask
6. MySQL
7. React
8. Chart.js

## Key features: 
1. The user specifies a ticker as well as a start and end date. 
2. If the data does not already exist in the database, the daily price data is fetched using yfinance, which is then stored in a MySQL database.  
3. The program retrieves the data and uses HTML and Chart.js to graph the open, high, low, close, and volume price for the specified period.
4. On each graph, the 20-day and 50-day weighted moving averages are shown. 

## Screenshots of Project
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/182038425-87ce87cf-b79f-4228-919b-03ea7462a7f1.png">
<img width="1439" alt="image" src="https://user-images.githubusercontent.com/78711575/182038436-f4752b05-3107-4e2f-8faa-8881f9398668.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/176934431-46e918a9-3459-411c-8d38-c9573f6e2bc2.png">
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/78711575/176934462-59839bdf-77dc-468e-8298-fb50986fddca.png">
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/78711575/176934489-cb5ca56d-382b-4c6e-90f5-7189593e4ed2.png">
<img width="1438" alt="image" src="https://user-images.githubusercontent.com/78711575/176934511-3e3b2be6-f803-4e82-82fc-7c2e4de9caa5.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/176934536-b1e34d5c-4162-411d-992e-d37bc3550d19.png">
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/78711575/176934557-3a5a956b-3e49-4793-b35f-884be3d415d3.png">

### Flask Server Setup 

```sh
python3 -m venv venv (Set up the virtual environment)
. venv/bin/activate  (Activate the virtual environment)
pip3 install -r requirements.txt (Install the required packages)
python3 databaseBuild.py (Sets up the database schema)
python3 app.py
```

This will run the server on port 5000

##  Backend Environment variables 

| Variable    | Description                                 |
| ----------- | ------------------------------------------- |
| PYTHON_ENV  | `development` or `production`               |
| DB_HOST     | Host address of database                    |
| DB_DATABASE | Database name                               |
| DB_USER     | Username credential                         |
| DB_PASSWORD | Password credentials                        |

Note: Backend Environment variables can be supplied via a `.env` file in the root directory. See  `./example.env` for an example 

### Frontend React Setup
```sh
cd ./client
npm install
npm start
```

This will run the application on port 3000. Open http://localhost:3000 to view it in your browser.

##  Frontend Environment variables 

| Variable    | Description                                 |
| ----------- | ------------------------------------------- |
| NODE_ENV    | `development`                               |

Note: Frontend Environment variables can be supplied via a `.env` file in the client directory. See  `./client/example.env` for an example 
