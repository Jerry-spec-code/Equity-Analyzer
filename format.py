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

def interpret_options_data(call_price, put_price):
    return {
        "status" : "success",
        "callPrice" : call_price,
        "putPrice" : put_price,
    }