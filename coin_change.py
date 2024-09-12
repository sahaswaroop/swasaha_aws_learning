def min_no_of_coin(coins,sum):
    coin_count=0
    total_coin_count=0
    for x in range(len(coins)):
        coin_count = sum//max(coins)
        sum = sum%max(coins)
        if max(coins) != min(coins):
            coins.remove(max(coins))
        total_coin_count = total_coin_count+coin_count
    print(total_coin_count)

coins=[1,5,6,9]
sum=11
min_no_of_coin(coins,sum)