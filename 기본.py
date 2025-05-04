import sys
from collections import Counter


input= sys.stdin.readline


#N=int(input())
# arr_N=list(map(int, input().split()))
#
# M=int(input())
# arr_M=list(map(int,input().split()))
#
# result=['1' if x in arr_N else '0' for x in arr_M]
# print(' '.join(result))

# N=list(map(int,input().split()))
# N=[list(map(int,input().split())) for _ in range(2)]
# print(N)
# numbers = [1, 2, 3]
#
# print(" ".join(map(str,numbers)))
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
print(arr)



