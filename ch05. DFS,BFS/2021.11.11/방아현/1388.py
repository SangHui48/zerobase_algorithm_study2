n, m = map(int, input().split())

graph = []

for _ in range(n):
	graph.append(list(input()))

visited = [[False] * m for _ in range(n)]

def dfs(i, j, visited):
	visited[i][j] = True
	if graph[i][j] == '-':
		if j + 1 < m and graph[i][j + 1] == '-' and not visited[i][j + 1]:
			dfs(i, j + 1, visited)
	elif graph[i][j] == '|':
		if i + 1 < n and graph[i + 1][j] == '|' and not visited[i + 1][j]:
			dfs(i + 1, j, visited)

result = 0
for i in range(n):
	for j in range(m):
		if not visited[i][j]:
			dfs(i, j, visited)
			result += 1

print(result)
