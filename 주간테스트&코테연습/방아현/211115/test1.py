def solution(no, works):
	if no > sum(works):
		return 0
	for i in range(no):
		works.sort()
		works[-1] -= 1
	return sum([i ** 2 for i in works])

print(solution(4, [4, 3, 3]))
