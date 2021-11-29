from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, start, visited):
	q = deque([start])
	visited[start[0]][start[1]] = 1
	while q:
		now = q.popleft()
		for i in range(4):
			x = now[0] + dx[i]
			y = now[1] + dy[i]
			if x >= 0 and y >= 0 and x < len(graph) and y < len(graph[0]) and \
				graph[x][y] != 0:
				if visited[x][y] == 0:
					visited[x][y] = visited[now[0]][now[1]] + 1
					q.append((x, y))


def solution(maps):
	visited = [[0] * len(maps[0]) for _ in range(len(maps))]
	bfs(maps, (0, 0), visited)
	if visited[-1][-1] == 0:
		return -1
	else:
		return visited[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
