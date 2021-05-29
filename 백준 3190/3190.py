# matrix  최대 사이즈 : 100 x 100 => 10000
# 최악의 경우 : 뱀이 끝까지 돌고 난 후에 자신의 몸과 부딪히는 경우
# 시간 복잡도 : O(N)
# y는 위 아래 --> Row / x는 왼, 오른쪽 --> col
# direction 회전 방향
from collections import deque
import sys
sys.stdin = open("input.txt")

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def iswall(x, y):
    if x < 0 or y < 0 :
        return False
    if x >= N or y >= N :
        return False
    if matrix[y][x] ==2 :
        return False
    return True

def bfs(dir,time,x,y):
    tail = deque([(y, x)])  # 방문 위치
    matrix[y][x] = 2
    while True:
        y, x = y + dy[dir], x + dx[dir]
        if iswall(x,y):
            if not matrix[y][x] == 1:  # 사과가 없는 경우 --> 길이 그대로
                temp_y, temp_x = tail.popleft()
                matrix[temp_y][temp_x] = 0  # 꼬리 제거
            matrix[y][x] = 2
            tail.append((y, x))
            if time in time_list:
                dir = turn(dir, time_list[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time
def turn(dir, turn):
    if turn =="L": # 왼쪽으로 돌기
        dir = (dir +3) %4
    else : # 오른쪽으로 돌기
        dir = (dir+1) %4
    return dir
# -----------------------------------------initialize -----------------------------------------
# matrix size
N = int(input())
matrix = [[0] * N for _ in range(N)]

# number of apple
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1  # 사과 좌표
# 뱀의 방향 변환 정보
L = int(input())
time_list = dict()
for i in range(L): # X : 시간, C : 방향
    X, C = input().split()
    time_list[int(X)] = C
print(bfs(1,1,0,0))