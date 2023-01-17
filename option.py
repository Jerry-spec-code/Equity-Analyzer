import random
import math

class Option:
    def __init__(self, underlyingPrice, strikePrice, interestRate, volatility, expires):
        self.S = underlyingPrice
        self.K = strikePrice
        self.r = interestRate
        self.v = volatility
        self.T = expires
        self.numSims = 1000000

    def getOptionsData(self):
        callPrice = self.monteCarloCallOrPutPrice(False)
        putPrice = self.monteCarloCallOrPutPrice(True)
        return callPrice, putPrice

    def monteCarloCallOrPutPrice(self, put):
        S_adjust = self.S * math.exp(self.T*(self.r-0.5*self.v*self.v))
        S_cur = 0.0
        payoffSum = 0.0

        for i in range(0, self.numSims):
            gauss_bm = self.gaussianBoxMuller()
            S_cur = S_adjust * math.exp(math.sqrt(self.v * self.v * self.T) * gauss_bm)
            difference = S_cur - self.K
            if put:
                difference *= -1
            payoffSum += max(difference, 0.0)
        
        return (payoffSum / self.numSims) * math.exp(-1 * self.r * self.T)

    def gaussianBoxMuller(self):
        x = 0.0
        y = 0.0
        euclidSq = 1.0
        # Continue generating two uniform random variables
        # until their coordinates lie within the unit circle 
        while euclidSq >= 1.0:
            x = self.getRandomNumber(-1, 1)
            y = self.getRandomNumber(-1, 1)
            euclidSq = x * x + y * y

        return x * math.sqrt(-2 * math.log(euclidSq) / euclidSq) 

    def getRandomNumber(self, lower, higher):
        return random.uniform(lower, higher)
