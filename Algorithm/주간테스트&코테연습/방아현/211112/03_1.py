

def divide(arr, a, b):
	if len(arr) == 1:
		return 1
	mid = len(arr) // 2
	rst = min(divide(arr[:mid], a, b), divide(arr[mid:], a, b))
	if a in arr and b in arr:
		return rst
	else:
		return rst + 1

def solution(n, a, b):
	array = [i for i in range(1, n + 1)]
	return divide(array, a, b)


print(solution(8, 4, 7))
print(solution(8, 1, 7))
