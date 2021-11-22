# Link: http://www.geeksforgeeks.org/stock-buy-sell/
class Interval:
    def __init__(self):
        self.buy = None
        self.sell = None


def stockBuySell(price, n):

    # There must at least be 2 days of price
    if n == 1:
        return

    count = 0
    sol = [Interval() for i in range(int(n / 2 + 1))]
    i = 0
    while i < n - 1:
        # Find Local Minima. Note that the limit is (n-2) as we are
        # comparing present element to the next element.
        while (i < n - 1) and (price[i] >= price[i + 1]):
            i += 1

        # If we reached the end, break as no further solution possible
        if i == n - 1:
            break

        # Store the index of minima
        sol[count].buy = i
        i += 1

        # Find Local Maxima.  Note that the limit is (n-1) as we are
        # comparing to previous element
        while (i < n) and (price[i] >= price[i - 1]):
            i += 1

        # Store the index of maxima
        sol[count].sell = i - 1

        # Increment count of buy/sell pairs
        count += 1

    if count == 0:
        print("There is no day when buying the stock will make profit")
    else:
        for i in range(count):
            print("Buy on day:", sol[i].buy, "\t", "Sell on day:", sol[i].sell)


# test 1
price = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(price, len(price))

# test 2
price = []
stockBuySell(price, len(price))

# test 3
price = [1]
stockBuySell(price, len(price))

price = [200, 1, 40]
stockBuySell(price, len(price))
