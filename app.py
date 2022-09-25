from tracemalloc import start
from turtle import st
from flask import Flask, render_template, request, escape
from flask_cors import CORS
import loadPrices as lp
import datetime 
import trend as tr
import service as s

app = Flask(__name__)
CORS(app)

# Need to setup frontend to run 
@app.route('/api')
def getAllData():
    try: 
        inputData = request.json
        my_ticker = inputData["ticker"]
        startDate = inputData["startDate"]
        endDate = inputData["endDate"]
        data = lp.getPriceData(my_ticker, startDate, endDate)
        return s.interpretAllData(data)
    except Exception as e:
        return {"status": "Error: " + e}

# Runs on localhost:5000
@app.route('/')
def index():
    if 'get_data' in request.args: #If the button was clicked
        my_ticker = str(escape(request.args.get("ticker", "")))
        if not my_ticker or my_ticker == "":
            return render_template("index.html", msg = "Please enter a valid ticker.")
        startDate = str(escape(request.args.get("startDate", "")))
        if not startDate or startDate == "":
            return render_template("index.html", default_ticker = my_ticker, msg = "Please enter a valid start date.")
        endDate = str(escape(request.args.get("endDate", "")))
        if not endDate or endDate == "":
            return render_template("index.html", default_ticker = my_ticker, default_startDate = startDate, 
                                                msg = "Please enter a valid end date.")

        convertedStartDate = datetime.datetime.strptime(startDate, '%Y-%m-%d') 
        convertedEndDate = datetime.datetime.strptime(endDate, '%Y-%m-%d') 
        if convertedStartDate > convertedEndDate:
            return render_template("index.html", msg = "Start date must be earlier than end date")
        
        data = lp.getPriceData(my_ticker, startDate, endDate)

        return render_template("index.html", 
                                default_ticker = my_ticker,
                                default_startDate = startDate,
                                default_endDate = endDate,
                                msg = "See the trend below for " + my_ticker + ":", 

                                x_graph1 = data[0],
                                y1_graph1 = data[1],
                                y2_graph1 = tr.movingAverage(data[1], 20),
                                y3_graph1 = tr.movingAverage(data[1], 50),

                                x_graph2 = data[0],
                                y1_graph2 = data[2],
                                y2_graph2 = tr.movingAverage(data[2], 20),
                                y3_graph2 = tr.movingAverage(data[2], 50),

                                x_graph3 = data[0],
                                y1_graph3 = data[3],
                                y2_graph3 = tr.movingAverage(data[3], 20),
                                y3_graph3 = tr.movingAverage(data[3], 50),

                                x_graph4 = data[0],
                                y1_graph4 = data[4],
                                y2_graph4 = tr.movingAverage(data[4], 20),
                                y3_graph4 = tr.movingAverage(data[4], 50),

                                x_graph5 = data[0],
                                y1_graph5 = data[5],
                                y2_graph5 = tr.movingAverage(data[5], 20),
                                y3_graph5 = tr.movingAverage(data[5], 50),

                                x_graph6 = data[0],
                                y1_graph6 = data[6],
                                y2_graph6 = tr.movingAverage(data[6], 20),
                                y3_graph6 = tr.movingAverage(data[6], 50))

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)