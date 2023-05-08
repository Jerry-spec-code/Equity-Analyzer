import random
import math
from scipy.stats import norm

class Option:
    def __init__(self, underlying_price, strike_price, interest_rate, volatility, expires):
        self.S = underlying_price
        self.K = strike_price
        self.r = interest_rate
        self.v = volatility
        self.T = expires
        self.num_sims = 1000000

    def get_black_scholes_option_prices(self):
        try:
            common_value = self.v * math.sqrt(self.T)
            d1 = (math.log(self.S / self.K) + self.T * (self.r + self.v * self.v / 2)) / common_value
            d2 = d1 - common_value

            factor_one = self.S
            factor_two = self.K * math.exp(-1 * self.r * self.T)
            call_price = factor_one * norm.cdf(d1) - factor_two * norm.cdf(d2)
            put_price = factor_two * norm.cdf(-1 * d2) - factor_one * norm.cdf(-1 * d1) 

        except:
            call_price = None
            put_price = None

        return call_price, put_price

    def get_monte_carlo_option_prices(self):
        call_price = self.monte_carlo_price(option_type="call")
        put_price = self.monte_carlo_price(option_type="put")

        return call_price, put_price

    def monte_carlo_price(self, option_type="call"):
        S_adjust = self.S * math.exp(self.T * (self.r - 0.5 * self.v * self.v))
        S_cur = 0.0
        payoff_sum = 0.0

        for _ in range(self.num_sims):
            gauss_bm = self.gaussian_box_muller()
            S_cur = S_adjust * math.exp(math.sqrt(self.v * self.v * self.T) * gauss_bm)
            difference = S_cur - self.K
            if option_type == "put":
                difference *= -1
            payoff_sum += max(difference, 0.0)
        
        return (payoff_sum / self.num_sims) * math.exp(-1 * self.r * self.T)

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

        return x * math.sqrt(-2 * math.log(euclid_sq) / euclid_sq) 

    def get_random_number(self, lower, higher):
        return random.uniform(lower, higher)
