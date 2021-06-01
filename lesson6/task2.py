# Task 2. Computes and returns the total price of stock
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
individual_price = {key: prices[key] * stock[key] for key in prices}
total_price = sum({prices[key] * stock[key] for key in prices})
print(individual_price, total_price, sep=" = ")
