def change(price):
    coins = [500, 100, 50, 10, 5, 1]

    change = 1000 - price
    coin_count = 0

    for coin in coins:
        coin_count += change // coin
        change %= coin

    return coin_count

price = int(input())
print(change(price))