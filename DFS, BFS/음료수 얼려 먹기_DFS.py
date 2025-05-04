import sys

input = sys.stdin.readline

n, m =map(int, input().split())

ice_graph=[list(map(int, input().strip())) for _ in range (n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if ice_graph[x][y] == 0:
        ice_graph[x][y] = 1             #방문 노드가 빈 칸이라면 1로 채워준다.

        for i in range(4):              #방문 노드가 빈 칸이라면 노드 기준 상하좌우 모두 1로 채운다.
            nx= x+dx[i]
            ny= y+dy[i]
            dfs(nx,ny)

        return True                     #방문 노드 기준 연쇄되는 빈 노드는 모두 1로 채워 졌으므로 하나의 아이스크림이 만들어진다.
    return False    #방문 노드가 채워져있을 경우.

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1

print(result)