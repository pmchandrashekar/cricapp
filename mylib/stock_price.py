def stock(prices):
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# Driver code 
if __name__ == '__main__':
    print(stock([1,2,0,3])) # answer should be 5, the person purchased the stock on 1st day and sold it on 5th day to make max profit
