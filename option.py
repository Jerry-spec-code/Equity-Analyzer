import random
import numpy as np
from scipy.stats import norm

class OptionConstants:
    @staticmethod
    def call_string():
        return "call"
    
    @staticmethod
    def put_string():
        return "put"

class Option:
    def __init__(self, underlying_price, strike_price, interest_rate, volatility, expires):
        self.S = underlying_price
        self.K = strike_price
        self.r = interest_rate
        self.v = volatility
        self.T = expires
        self.num_sims = 1000000
        self.sensitivity_factor = 0.01
        self.days_in_one_year = 365

    def get_option_greeks(self):
        greek_options_functions_map = {
            "delta" : self.get_delta,
            "gamma" : self.get_gamma,
            "vega" : self.get_vega,
            "theta" : self.get_theta,
            "rho" : self.get_rho,
        }
        option_type_map = {
            "Call" : OptionConstants.call_string(),
            "Put" : OptionConstants.put_string(),
        }
        res = {}
        for greek, greek_function in greek_options_functions_map.items():
            for option_type_key, option_type_value in option_type_map.items():
                res[greek + option_type_key] = greek_function(option_type=option_type_value)
        return res

    def get_delta(self, option_type=OptionConstants.call_string()):
        try:
            d1, _ = self.calculate_d1_d2()
            if option_type == OptionConstants.call_string():
                return norm.cdf(d1)     
            elif option_type == OptionConstants.put_string(): 
                return -norm.cdf(-d1)
            else:
                raise Exception("Invalid option type")
        except:
            return None
        
    def get_gamma(self, option_type=OptionConstants.call_string()):
        try:
            d1, _ = self.calculate_d1_d2()
            return norm.pdf(d1) / (self.S * self.v * np.sqrt(self.T))
        except:
            return None 

    def get_vega(self, option_type=OptionConstants.call_string()):
        try:
            d1, _ = self.calculate_d1_d2()
            return self.S * norm.pdf(d1) * np.sqrt(self.T) * self.sensitivity_factor
        except:
            return None 

    def get_theta(self, option_type=OptionConstants.call_string()):
        try:
            d1, d2 = self.calculate_d1_d2()
            firstTerm = -self.S * norm.pdf(d1) * self.v / (2 * np.sqrt(self.T))
            if option_type == OptionConstants.call_string():
                secondTerm = -self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
                return (firstTerm + secondTerm) / self.days_in_one_year
            elif option_type == OptionConstants.put_string():
                secondTerm = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
                return (firstTerm + secondTerm) / self.days_in_one_year
            else:
                raise Exception("Invalid option type")
        except:
            return None 

    def get_rho(self, option_type=OptionConstants.call_string()):
        try:
            _, d2 = self.calculate_d1_d2()
            if option_type == OptionConstants.call_string():
                return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2) * self.sensitivity_factor
            elif option_type == OptionConstants.put_string():
                return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2) * self.sensitivity_factor
            else:
                raise Exception("Invalid option type")
        except:
            return None 

    def get_black_scholes_option_prices(self):
        try:
            d1, d2 = self.calculate_d1_d2()
            factor_one = self.S
            factor_two = self.K * np.exp(-1 * self.r * self.T)
            call_price = factor_one * norm.cdf(d1) - factor_two * norm.cdf(d2)
            put_price = factor_two * norm.cdf(-1 * d2) - factor_one * norm.cdf(-1 * d1) 

        except:
            call_price = None
            put_price = None

        return call_price, put_price
    
    def calculate_d1_d2(self):
        common_value = self.v * np.sqrt(self.T)
        d1 = (np.log(self.S / self.K) + self.T * (self.r + self.v * self.v / 2)) / common_value
        d2 = d1 - common_value
        return d1, d2

    def get_monte_carlo_option_prices(self):
        call_price = self.monte_carlo_price(option_type=OptionConstants.call_string())
        put_price = self.monte_carlo_price(option_type=OptionConstants.put_string())

        return call_price, put_price

    def monte_carlo_price(self, option_type=OptionConstants.call_string()):
        S_adjust = self.S * np.exp(self.T * (self.r - 0.5 * self.v * self.v))
        S_cur = 0.0
        payoff_sum = 0.0

        for _ in range(self.num_sims):
            gauss_bm = self.gaussian_box_muller()
            S_cur = S_adjust * np.exp(np.sqrt(self.v * self.v * self.T) * gauss_bm)
            difference = S_cur - self.K
            if option_type == OptionConstants.put_string():
                difference *= -1
            payoff_sum += max(difference, 0.0)
        
        return (payoff_sum / self.num_sims) * np.exp(-1 * self.r * self.T)

    def gaussian_box_muller(self):
        x = 0.0
        y = 0.0
        euclid_sq = 1.0
        # Continue generating two uniform random variables
        # until their coordinates lie within the unit circle 
        while euclid_sq >= 1.0:
            x = self.get_random_number(-1, 1)
            y = self.get_random_number(-1, 1)
            euclid_sq = x * x + y * y

        return x * np.sqrt(-2 * np.log(euclid_sq) / euclid_sq) 

    def get_random_number(self, lower, higher):
        return random.uniform(lower, higher)
