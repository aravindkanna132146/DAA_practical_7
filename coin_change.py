def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 3, 4]
amount = 6

result = coin_change(coins, amount)

print("Minimum coins:", result)

