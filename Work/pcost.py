# pcost.py
#
# Exercise 1.32
import csv


def portfolio_cost(filename):
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        num_shares = 0.0
        price = 0.0

        for row in rows:
            try:
                num_shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("Couldn't parse", row)

            total += num_shares * price

    return total


cost = portfolio_cost('Work/Data/missing.csv')
cost = portfolio_cost('Work/Data/portfolio.csv')
print(f'Total cost: {cost}')
