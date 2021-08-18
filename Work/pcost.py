# pcost.py
#
# Exercise 1.33
import csv


def portfolio_cost(filename):
    """Get the total cost of a portfolio file

    Args:
        filename (string): path to file

    Returns:
        int: Total cost
    """
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        for row in rows:
            try:
                num_shares = int(row[1])
                price = float(row[2])
                total += num_shares * price
            except ValueError:
                print("Couldn't parse", row)

    return total

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename with path:')
    
cost = portfolio_cost('Work/Data/missing.csv')
cost = portfolio_cost('Work/Data/portfolio.csv')
print(f'Total cost: {cost}')
