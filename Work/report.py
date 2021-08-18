# report.py
#
# Exercise 2.5
import sys
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
                print("Couldn't parse", row)

    return portfolio


cost = read_portfolio('Work/Data/portfolio.csv')
print(f'Total cost: {cost}')
