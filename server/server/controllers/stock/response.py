import server.services.trend.trend as tr

def object_from_inputs(ticker, start_date, end_date):
    return {
        'ticker': ticker,
        'start_date': start_date,
        'end_date': end_date,
    }

def interpret_daily_price_data(data):
    possible_graphs = ["", "Opening", "High", "Low", "Closing", "AdjClose", "Volume"]
    res = {}
    res["x-data"] = data[0]
    for i, title in enumerate(possible_graphs):
        if i == 0: #x-axis data
            continue 
        res[title] = format_daily_price_data_with_moving_averages(data[i])
    return res

def format_daily_price_data_with_moving_averages(data):
    return {
        "y-data" : data,
        "20-day-average" : tr.moving_average(data, 20),
        "50-day-average" : tr.moving_average(data, 50),
    }
