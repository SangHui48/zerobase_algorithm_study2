def solution(n):
	n_to_str = str(n)
	result = 0
	for c in n_to_str:
		result += int(c)
	return result

print(solution(131))
