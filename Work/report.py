# report.py
#
# Exercise 2.4
import sys
import csv


def read_portfolio(filename):
    """Read a stock portfolio file

    Args:
        filename (string): path to file

    Returns:
        list of tuples: Portfolio
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        for row in rows:
            try:
                stock = (row[0], int(row[1]), float(row[2]))
                portfolio.append(stock)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = read_portfolio('Work/Data/missing.csv')
cost = read_portfolio('Work/Data/portfolio.csv')
print(f'Total cost: {cost}')
