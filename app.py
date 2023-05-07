from tracemalloc import start
from turtle import st
from flask import Flask, render_template, request, escape
from flask_cors import CORS
import loadPrices as lp
import datetime 
import trend as tr
import format as f
import option as op

app = Flask(__name__)
CORS(app)

# Need to setup frontend to run 
@app.route('/api', methods=['POST'])
def get_daily_price_data():
    try: 
        input_data = request.json
        my_ticker = input_data["ticker"]
        start_date = f.process_date(input_data["startDate"])
        end_date = f.process_date(input_data["endDate"])
        data = lp.get_daily_price_data(my_ticker, start_date, end_date)
        return f.interpret_daily_price_data(data)
    except Exception as e:
        return {"status": "Error: " + str(e)}
 
@app.route('/api/options', methods=['POST'])
def get_options_data():
    try: 
        input_data = request.json
        underlying_price = f.string_to_float(input_data["underlyingPrice"])
        strike_price = f.string_to_float(input_data["strikePrice"])
        interest_rate = f.string_to_float(input_data["interestRate"]) # Risk-free rate 
        volatility = f.string_to_float(input_data["volatility"]) # Volatility of the underlying (20%)
        expires = f.string_to_float(input_data["expires"]) # Years until expiry
        option = op.Option(underlying_price, strike_price, interest_rate, volatility, expires)
        call_price, put_price = option.get_options_data()
        return f.interpret_options_data(call_price, put_price)
    except Exception as e:
        return {"status": "Error: " + str(e)}

# Runs on localhost:5000
@app.route('/')
def index():
    if 'get_data' in request.args: #If the button was clicked
        my_ticker = str(escape(request.args.get("ticker", "")))
        if not my_ticker or my_ticker == "":
            return render_template("index.html", msg = "Please enter a valid ticker.")
        start_date = str(escape(request.args.get("startDate", "")))
        if not start_date or start_date == "":
            return render_template("index.html", default_ticker = my_ticker, msg = "Please enter a valid start date.")
        end_date = str(escape(request.args.get("endDate", "")))
        if not end_date or end_date == "":
            return render_template("index.html", default_ticker = my_ticker, default_startDate = start_date, 
                                                msg = "Please enter a valid end date.")

        converted_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d') 
        converted_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') 
        if converted_start_date > converted_end_date:
            return render_template("index.html", msg = "Start date must be earlier than end date")
        
        data = lp.get_daily_price_data(my_ticker, start_date, end_date)

        return render_template("index.html", 
                                default_ticker = my_ticker,
                                default_startDate = start_date,
                                default_endDate = end_date,
                                msg = "See the trend below for " + my_ticker + ":", 

                                x_graph1 = data[0],
                                y1_graph1 = data[1],
                                y2_graph1 = tr.moving_average(data[1], 20),
                                y3_graph1 = tr.moving_average(data[1], 50),

                                x_graph2 = data[0],
                                y1_graph2 = data[2],
                                y2_graph2 = tr.moving_average(data[2], 20),
                                y3_graph2 = tr.moving_average(data[2], 50),

                                x_graph3 = data[0],
                                y1_graph3 = data[3],
                                y2_graph3 = tr.moving_average(data[3], 20),
                                y3_graph3 = tr.moving_average(data[3], 50),

                                x_graph4 = data[0],
                                y1_graph4 = data[4],
                                y2_graph4 = tr.moving_average(data[4], 20),
                                y3_graph4 = tr.moving_average(data[4], 50),

                                x_graph5 = data[0],
                                y1_graph5 = data[5],
                                y2_graph5 = tr.moving_average(data[5], 20),
                                y3_graph5 = tr.moving_average(data[5], 50),

                                x_graph6 = data[0],
                                y1_graph6 = data[6],
                                y2_graph6 = tr.moving_average(data[6], 20),
                                y3_graph6 = tr.moving_average(data[6], 50))

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)