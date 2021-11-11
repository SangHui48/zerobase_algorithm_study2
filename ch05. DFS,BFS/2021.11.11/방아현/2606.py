n = int(input()) #컴퓨터수
m = int(input()) #네트워크수

networks = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
	i, j = map(int, input().split())
	networks[i][j] = networks[j][i] = 1

computers = [False] * (n + 1)

def bfs(i, computers):
	for j in range(len(networks[i])):
		if networks[i][j] == 1 and not computers[j]:
			computers[j] = True
			bfs(j, computers)

computers[1] = True
bfs(1, computers)
print(computers.count(True) - 1)
