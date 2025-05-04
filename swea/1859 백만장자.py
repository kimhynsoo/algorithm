from collections import deque
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    # day = int(input())
    # prices = deque(map(int, input().split()))
    # max_price = max(prices)
    # max_index = prices.index(max_price)
    # result = 0
    # while prices:
    #     max_price = max(prices)
    #     max_index = prices.index(max_price)
    #     for i in range(max_index):
    #         result += max_price - prices.popleft()
    #     prices.popleft()
    # print(result)
    day=int(input())
    prices=list(map(int,input().split()))[::-1]
    answer=0
    max=0
    for price in prices:
        if price>max:
            max= price
        else:
            answer+=max-price
    print(answer)

