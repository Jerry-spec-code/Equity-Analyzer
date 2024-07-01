from server.controllers.option.response import object_from_inputs, add_monte_carlo_to_data, add_black_scholes_to_data, add_option_greeks_to_data
from server.controllers.common.common import success
from server.services.option.option import Option

def get_option_price_data(req, res):
    data = {}
    inputs = input_validation(req, res)
    option_object = Option(inputs)

    if inputs['run_monte_carlo']:
        monte_carlo_call_price, monte_carlo_put_price = option_object.get_monte_carlo_option_prices()
        add_monte_carlo_to_data(data, monte_carlo_call_price, monte_carlo_put_price)

    black_scholes_call_price, black_scholes_put_price = option_object.get_black_scholes_option_prices()
    add_black_scholes_to_data(data, black_scholes_call_price, black_scholes_put_price)

    option_greeks = option_object.get_option_greeks()
    add_option_greeks_to_data(data, option_greeks)

    return success(data, res)
    
def input_validation(req, res):
    try:
        input_data = req.json
        run_monte_carlo = input_data["runMonteCarlo"]
        underlying_price = float(input_data["underlyingPrice"])
        strike_price = float(input_data["strikePrice"])
        interest_rate = float(input_data["interestRate"]) # Risk-free rate 
        volatility = float(input_data["volatility"]) # Volatility of the underlying (20%)
        expiry = float(input_data["expires"]) # Years until expiry
        return object_from_inputs(
            underlying_price, 
            strike_price, 
            interest_rate, 
            volatility, 
            expiry, 
            run_monte_carlo
        )
    except:
        return res({"status": "Error: Invalid float from string for option price"}), 400