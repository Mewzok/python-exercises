# def apply_discount_to_expensive_items(prices):
#     discount = .10
#     updated_prices = []

#     for price in prices:
#         if price > 10:
#             price = price * (1 - discount)
        
#         updated_prices.append(price)

#     return updated_prices

def apply_discount_to_expensive_items(prices):
    discount = .10

    return [price * (1 - discount) if price > 10 else price for price in prices]

prices = [5, 12, 30, 8, 25]

print(apply_discount_to_expensive_items(prices))