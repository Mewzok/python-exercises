# def apply_discount(prices):
#     discount = .10
#     discounted_prices = []
    
#     for price in prices:
#         discounted_price = price * (1 - discount)
#         discounted_prices.append(discounted_price)

#     return discounted_prices

def apply_discount(prices):
    discount = .10
    
    return [price * (1 - discount) for price in prices]

prices = [10, 20, 30]

print(apply_discount(prices))