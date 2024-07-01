def object_from_inputs(underlying_price, strike_price, interest_rate, volatility, expiry, run_monte_carlo):
    return {
        'underlying_price': underlying_price,
        'strike_price': strike_price,
        'interest_rate': interest_rate,
        'volatility': volatility,
        'expiry': expiry,
        'run_monte_carlo': run_monte_carlo,
    }

def add_monte_carlo_to_data(data, monte_carlo_call_price, monte_carlo_put_price):
    data['monteCarloCallPrice'] = monte_carlo_call_price
    data['monteCarloPutPrice'] = monte_carlo_put_price

def add_black_scholes_to_data(data, black_scholes_call_price, black_scholes_put_price):
    data['blackScholesCallPrice'] = black_scholes_call_price
    data['blackScholesPutPrice'] = black_scholes_put_price

def add_option_greeks_to_data(data, option_greeks):
    data.update(option_greeks)
