# pcost.py
#
# Exercise 1.27

total = 0.0

with open('Work/Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')
        num_shares = int(row[1])
        price = float(row[2])
        total += num_shares * price

print(f'Total cost: {total}')
