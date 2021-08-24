# report.py
#
# Exercise 2.11
import csv


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


def make_report(portfolio, prices):
    total_cost = 0.0

    for stock in portfolio:
        total_cost += stock['price'] * stock['shares']

    print(f'Total cost: {total_cost}')

    total_value = 0.0
    for stock in portfolio:
        total_value += prices[stock['name']] * stock['shares']

    print(f'Total value: {total_value}')
    print(f'Gain: {(total_value - total_cost):0.2f}')

    return total_value


portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')
data = make_report(portfolio, prices)

print(f'Data: {data}')
