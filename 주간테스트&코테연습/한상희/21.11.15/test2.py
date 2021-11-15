from collections import deque

def solution(maps):
    answer = -1
    dx = [-1, 1, 0, 0] # U D L R
    dy = [0, 0, -1, 1]
    width = len(maps[0])
    height = len(maps)
    queue = deque()
    queue.append((0, 0)) #초기 위치 1행 1열

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖으로 벗어나는 경우
            if nx < 0 or nx >= height or ny < 0 or ny >= width:
                continue
            # 벽일경우
            if maps[nx][ny] == 0:
                continue
            # 처음 방문하는 곳일 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    if maps[height-1][width-1] == 1:
        return -1
    else:
        return maps[height-1][width-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))