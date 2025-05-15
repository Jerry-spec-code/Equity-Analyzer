# Equity-Analyzer
A Flask web application that tracks real-time equity prices for different companies in a MySQL database, graphs important statistical trends using React/Chart.js, integrated with a Black Scholes and Monte Carlo option pricing calculator.

# Project Demo
https://youtu.be/jVuRS5mW1XA

## Languages/Tools/Frameworks used: 
1. Python
2. SQL
3. TypeScript
4. HTML/CSS
5. Flask
6. MySQL
7. React
8. Chart.js
9. Makefile

## Key features: 
1. The user specifies a ticker as well as a start and end date. 
2. If the data does not already exist in the database, the daily price data is fetched using yfinance, which is then stored in a MySQL database.  
3. The program retrieves the data and uses React and Chart.js to graph the open, high, low, close, and volume price for the specified period.
4. On each graph, the 20-day (red line) and 50-day (blue line) weighted moving averages are shown. 
5. The option pricing calculator outputs the call and put prices from both the Black Scholes model as well as a Monte Carlo simultation given the underlying price, strike price, risk-free interest rate, volatility, and maturity, generating both theoretical prices and Greek values.

## Screenshots of Project

### Stock Market Trend Analyzer
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/78711575/236712767-0f7ba0b4-3af3-4d72-b527-0ce5c484eccf.png">

### Option Price Calculator
<img width="1440" alt="image" src="https://github.com/Jerry-spec-code/Equity-Analyzer/assets/78711575/05d24aa1-7012-4bab-8580-fb0dc60a4f35">

##  Backend Environment variables 

| Variable    | Description                                 |
| ----------- | ------------------------------------------- |
| PYTHON_ENV  | `development` or `production`               |
| DB_HOST     | Host address of database                    |
| DB_DATABASE | Database name                               |
| DB_USER     | Username credentials                        |
| DB_PASSWORD | Password credentials                        |

Note: Backend Environment variables can be supplied via a `.env` file in the server directory. See  `./server/example.env` for an example 

##  Frontend Environment variables 

| Variable    | Description                                 |
| ----------- | ------------------------------------------- |
| NODE_ENV    | `development`                               |

Note: Frontend Environment variables can be supplied via a `.env` file in the client directory. See  `./client/example.env` for an example

## Project Setup

To run the project, you will need to open two separate terminals.
- In the first terminal, run `make backend`. This will install all the Python packages in a virtual environment and run the server on port 5000.
- In the second terminal, run `make frontend`. This will install all the TypeScript packages and run the application on port 3000. Open http://localhost:3000 to view the result in your browser.

### Other Make Commands
| Command                  | Description                                                   |
| -----------------------  | ------------------------------------------------------------- |
| `make install_frontend`  | Install all the frontend TypeScript packages                  |
| `make start_frontend`    | Start the frontend without installing packages                |
| `make install_backend`   | Setup virtual environment and install backend Python packages |
| `make start_backend`     | Start the server without installing packages                  |
| `make clean_backend`     | Destroys the virtual environment and removes Python packages  |
