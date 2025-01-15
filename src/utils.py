import numpy as np

def compounded_interest(cash: float, interest_rate: float, periods: float):
    return cash * (1 + interest_rate)**periods


def present_value_single(cash: float, discount_rate: float, periods: float):
    return compounded_interest(cash, discount_rate, -periods)



def present_value_cash_flow(cash_flows: np.array, discount_rate: float, periods: np.array):
    return cash_flows / ((1 + discount_rate)**periods)