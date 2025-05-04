import sys

input = sys.stdin.readline

n,m=map(int,input().split())
seen=set(input().strip() for _ in range(n))
heard=set(input().strip() for _ in range(m))

both=sorted(seen&heard)
print(len(both))
print('\n'.join(both),end='')