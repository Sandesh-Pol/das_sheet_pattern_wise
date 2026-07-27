def max_profit_on_stock(prices):

    max_profit = 0

    for i in range(len(prices)):

        for j in range(i + 1, len(prices)):

            profit = prices[j] - prices[i]

            max_profit = max(max_profit, profit)

    return max_profit



def maxProfit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit

print(max_profit_on_stock([7,1,5,3,6,4]))
