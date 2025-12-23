coins = [1, 2, 5, 10]
amount = 23
coins.sort(reverse=True)
count = 0
for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1
print("Minimum coins needed:", count)
