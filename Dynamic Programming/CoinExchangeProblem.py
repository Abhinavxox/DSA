import sys

def min_coin_change(coins, value):
    t = [sys.maxsize]*(value+1)
    t[0] = 0

    for i in range(1,value+1):
        for j in coins:
            if j<=i:
                t[i] = min(t[i], t[i-j]+1)

    return t[value]

coins = [1, 2, 3, 5]
value = 10
print(min_coin_change(coins, value))
