import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
maze=[[0]*(m+1)]
for _ in range(n):
    maze.append([0]+list(map(int,input().strip())))

me=[[0]*(m+1) for _ in range(n+1)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def BFS(x,y):
    q=deque()
    q.append((x,y))
    while q:
        now_x,now_y=q.popleft() #BFS방식 주변 좌표를 꺼낸다.
        maze[now_x][now_y] = 0 #방문 표시. 벽으로 바꾼다.
        for i in range(4):
            new_x=now_x+dx[i]
            new_y=now_y+dy[i]
            if new_x>0 and new_x<=n and new_y>0 and new_y<=m and maze[new_x][new_y]==1:
                #new_x,new_y가 미로 공간을 벗어나지 않고 그 좌표가 길인 경우.
                q.append((new_x,new_y))
                me[new_x][new_y]=me[now_x][now_y]+1 #새로운 좌표에 이전 좌표의 이동값에+1 값을 넣는다.
                # for row in me:
                #     print(' '.join(str(x) for x in row))
                # print()

BFS(1,1)
print(me[n][m]+1)


