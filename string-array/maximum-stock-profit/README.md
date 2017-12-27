### Stock Buy Sell to Maximize Profit

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.

We are allowed to buy and sell multiple times

**Algorithms**:
```
1) Find the local minima and store it as starting index. If not exists, return.
2) Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3) Update the solution (Increment count of buy sell pairs)
4) Repeat the above steps if end is not reached.
```