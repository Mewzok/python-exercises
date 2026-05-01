def get_affordable_prices(prices):
    return [price for price in prices if price < 20]

prices = [5, 12, 30, 8, 25, 3, 18]

print(get_affordable_prices(prices))