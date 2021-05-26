import sys
from collections import deque

sys.stdin = open("input.txt")

# 상 하 우 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def iswall(nx,ny): # 벽이 되는 조건
    if nx < 0 or ny < 0: # 좌표가 0 미만이 되는 경우
        return False
    if nx >= N or ny >= M: # 리스트를 넘는 경우
        return False
    return True

def solution(cnt,cctv_list,ans):

    if cnt == cctv_n: # 모든 CCTV 탐색했다면 사각지대 개수 세주기
        count = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] ==0 and visited[i][j] == 0:
                    count += 1
        return count

    x, y, c = cctv_list[cnt][0], cctv_list[cnt][1], cctv_list[cnt][2]
    for k in range(4): # CCTV 의 4방향 확인
        new_dir = []
        if c == 1: # 1번 CCTV : 현재 방향
            new_dir.append(k)
        elif c == 2: # 2번 CCTV : 현재 방향 + 반대 방향
            new_dir.append(k)
            new_dir.append((k + 2) % 4)
        elif c == 3: # 3번 CCTV : 현재 방향 + 왼쪽 90도 방향
            new_dir.append(k)
            new_dir.append((k + 3) % 4)
        elif c == 4: # 4번 CCTV : 현재 방향 + 반대 방향 + 왼쪽 90도 방향
            new_dir.append(k)
            new_dir.append((k + 3) % 4)
            new_dir.append((k + 2) % 4)
        elif c == 5: # 5번 CCTV : 4방향
            new_dir.append(k)
            new_dir.append((k + 3) % 4)
            new_dir.append((k + 1) % 4)
            new_dir.append((k + 2) % 4)

        q = deque()
        for d in new_dir: # CCTV 방향 개수 만큼 이동
            nx, ny = x + dx[d], y + dy[d]
            while iswall(nx,ny): # 특정 방향으로 끝까지 이동
                if not visited[nx][ny] and matrix[nx][ny] != 6: # 방문하지 않았으며 벽이 아니면
                    visited[nx][ny] = 1# 방문
                    q.append((nx, ny))
                elif matrix[nx][ny] == 6: break # 벽이면 중단
                nx += dx[d]
                ny += dy[d]
        # 다음 CCTV 호출
        ans = min(ans, solution(cnt + 1,cctv_list,ans ))
        # 방문했던 곳 되돌려주기
        while q:
            qx, qy = q.popleft()
            if matrix[qx][qy] == 0:
                visited[qx][qy] = False
        # 5번 CCTV 는 회전할 필요 없으므로 바로 break
        if matrix[x][y] == 5: break
    return ans

N,M = map(int,input().split()) # N: row 수 / M: col 수
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]# 방문 여부 확인
cctv_list = [] # CCTV 좌표 리스트
cctv_n = 0 # 전체 CCTV 개수
ans = 0 # 사각지대

for i in range(N):
    for j in range(M):
        if 0 < matrix[i][j] < 6: # CCTV 발견하는 경우
            cctv_list.append((i, j,matrix[i][j]))
            visited[i][j] = True
            cctv_n += 1
        if matrix[i][j]== 0: # 사각지대 count --> MAX
            ans += 1
print(solution(0,cctv_list,ans))
