from server.services.stock.loadPrices import get_daily_price_data
from server.controllers.stock.response import interpret_daily_price_data, object_from_inputs
from server.controllers.common.common import success

def get_stock_data(req, res):
    inputs = input_validation(req, res)
    data = get_daily_price_data(inputs)
    stock_data = interpret_daily_price_data(data)
    return success(stock_data, res)

def input_validation(req, res):
    try:
        input_data = req.json
        ticker = input_data["ticker"]
        start_date = process_date(input_data["startDate"])
        end_date = process_date(input_data["endDate"])
        return object_from_inputs(ticker, start_date, end_date)
    except:
        return res({"status": "Error: Invalid ticker or start or end date"}), 400

def process_date(date):
    return date[0:date.find('T')] if date.find('T') != -1 else date
