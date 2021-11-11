from itertools import combinations

def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def solution(nums):
	array = list(combinations(nums, 3))
	result = 0
	for a in array:
		if isPrime(sum(a)):
			result += 1
	return result

print(solution([1, 2, 3, 4]))
print(solution([1, 2,7 ,6 ,4]))
