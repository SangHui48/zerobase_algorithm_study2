from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
	m1, m2 = map(int, input().split())
	graph[m1][m2] = graph[m2][m1] = 1

def bfs(start, visited):
	visited[start] = True
	q = deque([start])
	while q:
		now = q.popleft()
		print(now, end=' ')
		for i in range(len(graph[now])):
			if graph[now][i] == 1 and not visited[i]:
				visited[i] = True
				q.append(i)

def dfs(v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in range(len(graph[v])):
		if graph[v][i] == 1 and not visited[i]:
			visited[i] = True
			dfs(i, visited)

visited = [False] * (n + 1)
dfs(v, visited)
print()
visited = [False] * (n + 1)
bfs(v, visited)
