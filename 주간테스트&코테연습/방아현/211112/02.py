def solution(arr):
	arr.sort() # 오름차순으로 정렬
	for i in range(1, arr[-1] + 1):
		if i != arr[i-1]:
			return False
	return True

print(solution([4, 1, 3,2 ]))
