def maxProfit(prices: list[int]) -> int:
    mp = 0
    l = 0
    r = 1
    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            mp = max(mp, prices[r] - prices[l])

        r += 1

    return mp


t = [7,1,5,3,6,4]
m = maxProfit(t)
print(m)