# matrix 생성 --> 직사각형에 포함된 경우에는 1 표시
from collections import deque
import sys
sys.stdin = open("input.txt")

list_count = [] # 분리된 곳의 각각의 count
global count #  0이 연속해서 있는 경우 사각형의 갯수

# 상 하 우 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M,N,K = map(int,input().split()) # 행(y), 열(x), 사각형 갯수
matrix = [list(0 for _ in range(N)) for _ in range(M)]

for _ in range(K):
    left_x, left_y, right_x,right_y = map(int,input().split())
    for i in range(M-right_y,M-left_y):
        for j in range(left_x,right_x):
            matrix[i][j]=1
# print(matrix)
#------------------ initialized matrix ------------------------#

def iswall(x, y):
    if x < 0 or y < 0 :
        return False
    if x >= N or y >= M :
        return False
    if matrix[y][x] ==1 :
        return False
    return True

def bfs(end_x,end_y):
    queue = deque()
    queue.append((end_x,end_y))
    count = 1
    matrix[end_x][end_y] = 1 # 방문 표시
    while queue:
         y,x = queue.popleft()
         for i in range(4):
             nx, ny = x+dx[i], y+dy[i]
             if iswall(nx,ny):
                queue.append((ny,nx))
                count = count+1
                matrix[ny][nx] = 1
    return count

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            list_count.append(bfs(i,j))
# print(list_count)
print(len(list_count))
new_list = sorted(list_count)
for i in new_list:
    print(i,end=" ")