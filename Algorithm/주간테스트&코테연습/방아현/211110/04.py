def solution(dirs):
	graph = {}
	for i in range(5, -6, -1):
		for j in range(-5, 6):
			graph[(i, j)] = [0, 0, 0, 0]
	# 상, 좌, 하, 우
	dir_c = ['U', 'L', 'D', 'R']
	dir_x = [1, 0, -1, 0]
	dir_y = [0, -1, 0, 1]

	# 시작좌표
	pos = (0, 0)
	result = 0
	for d in dirs:
		idx = dir_c.index(d)
		x, y = pos[0] + dir_x[idx], pos[1] + dir_y[idx]
		if x < -5 or x > 5 or y < -5 or y > 5:
			continue
		if graph[pos][idx] == 0:
			result += 1
			graph[pos][idx] += 1
			graph[(x, y)][idx-2] += 1
		pos = (x, y)

	return result

print(solution("LR"))
