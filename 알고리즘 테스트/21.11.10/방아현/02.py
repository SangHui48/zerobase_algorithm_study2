def solution(arr):
	prev = arr[0]
	result = [prev, ]
	for i in range(1, len(arr)):
		if prev != arr[i]:
			prev = arr[i]
			result.append(prev)
	return result

print(solution([1, 1, 3, 3, 0, 1, 1]))
