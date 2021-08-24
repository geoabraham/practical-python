# report.py
#
# Exercise 2.16
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

        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                stock = {'name': record['name'],
                         'shares': int(record['shares']),
                         'price': float(record['price'])}
                portfolio.append(stock)
            except ValueError:
                print(f'read_portfolio(filename) :: Row {row_num}: Bad row: {row}')

    return portfolio


def read_prices(filename):
    """Read prices of stocks from file

    Args:
        filename (string): filename

    Returns:
        list of dictionary: prices
    """
    stock_prices = {}
    header = ['name', 'price']
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row_num, row in enumerate(rows,start=1):
            record = dict(zip(header, row))
            try:
                stock_prices[record['name']] = float(record['price'])
            except IndexError:
                print(f'read_prices(filename) :: Row {row_num}: Bad row: {row}')
            except KeyError:
                print(f'read_prices(filename) :: Row {row_num}: Bad row: {row}')

    return stock_prices


def get_report_data(portfolio, prices):
    """Get a list of tuples given a portfolio and stock prices

    Args:
        portfolio (list): a portfolio
        prices (dict): stock prices

    Returns:
        [list]: list of tuples (name, shares, price, change)
    """
    report_data = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        report_data.append(
            (stock['name'], stock['shares'], current_price, change))

    return report_data


def make_total_report(portfolio, prices):
    """Make Report

    Args:
        portfolio (list): portfolio list
        prices (dict): stock prices

    Returns:
        list: report
    """
    total_cost = 0.0

    for stock in portfolio:
        total_cost += stock['price'] * stock['shares']

    print(f'Total cost: {total_cost}')

    total_value = 0.0
    for stock in portfolio:
        total_value += prices[stock['name']] * stock['shares']

    print(f'Total value: {total_value}')
    print(f'Gain: {(total_value - total_cost):0.2f}')


def make_report(data):
    """Make and print on screen stocks report

    Args:
        data (list): data
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for row in data:
        formated_price = f'${row[2]:.2f}'
        print(
            f'{row[0]:>10s} {row[1]:>10d} {formated_price:>10s} {row[3]:>10.2f}')


# Read files
portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')

# Get data
data = get_report_data(portfolio, prices)

# Make report
make_report(data)

report = make_total_report(portfolio, prices)
