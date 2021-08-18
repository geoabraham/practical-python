# report.py
#
# Exercise 2.6
import csv
from pprint import pprint


def read_portfolio(filename):
    """Read a stock portfolio file

    Args:
        filename (string): path to file

    Returns:
        list of dictionary: Portfolio
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        for row in rows:
            try:
                stock = {'name': row[0],
                         'shares': int(row[1]),
                         'price': float(row[2])}
                portfolio.append(stock)
            except ValueError:
                pass

    return portfolio


def read_prices(filename):
    """Read prices of stocks from file

    Args:
        filename (string): filename

    Returns:
        list of dictionary: prices
    """
    stock_prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return stock_prices


portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')
pprint(portfolio)
pprint(prices)
