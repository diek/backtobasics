
'''Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and
returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.'''

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# No "shorting"—you must buy before you sell. You may not buy and sell in the
# same time step (at least 1 minute must pass).


def get_best_profit(stock_prices_yesterday):

    # we'll greedily update min_price and best_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    best_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, stock in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = stock - min_price

        # update best_profit if we can do better
        best_profit = max(best_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, stock)

    return best_profit

print(get_best_profit(stock_prices_yesterday))
