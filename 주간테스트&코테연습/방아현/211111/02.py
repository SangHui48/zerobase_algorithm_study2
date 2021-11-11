from collections import deque

INF = int(1e9)

def solution(N, road, K):
	array = [[] for _ in range(N + 1)]
	village = [INF] * (N + 1)
	for n in road:
		array[n[0]].append([n[1], n[2]])
		array[n[1]].append([n[0], n[2]])
	q = deque([1,])
	village[1] = 0
	while q:
		now = q.popleft()
		for a in array[now]:
			next, cost = a
			if village[next] > village[now] + cost:
				village[next] = village[now] + cost
				q.append(next)

	result = 0
	for i in range(1, len(village)):
		if village[i] <= K:
			result += 1
	return result

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) #4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) #4
