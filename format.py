import trend as tr

def interpret_daily_price_data(data):
    possible_graphs = ["", "Opening", "High", "Low", "Closing", "AdjClose", "Volume"]
    res = {}
    res["x-data"] = data[0]
    for i, title in enumerate(possible_graphs):
        if i == 0: #x-axis data
            continue 
        res[title] = format_daily_price_data_with_moving_averages(data[i])
    res["status"] = "success"
    return res

def format_daily_price_data_with_moving_averages(data):
    return {
        "y-data" : data,
        "20-day-average" : tr.moving_average(data, 20),
        "50-day-average" : tr.moving_average(data, 50),
    }

def process_date(date):
    return date[0:date.find('T')] if date.find('T') != -1 else date

def string_to_float(string):
    try:
        res = float(string)
        return res
    except:
        raise Exception("Invalid input")

def interpret_options_data(monte_carlo_call_price, monte_carlo_put_price, black_scholes_call_price, black_scholes_put_price):
    
    if black_scholes_call_price is None:
        black_scholes_call_price = monte_carlo_call_price
    
    if black_scholes_put_price is None:
        black_scholes_put_price = monte_carlo_put_price

    return {
        "status" : "success",
        "monteCarloCallPrice" : monte_carlo_call_price,
        "monteCarloPutPrice" : monte_carlo_put_price,
        "blackScholesCallPrice" : black_scholes_call_price,
        "blackScholesPutPrice" : black_scholes_put_price,
    }