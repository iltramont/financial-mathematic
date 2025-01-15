import numpy as np

def compounded_interest(cash: float, interest_rate: float, periods: float):
    return cash * (1 + interest_rate)**periods


