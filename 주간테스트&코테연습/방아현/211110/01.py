def solution(nums):
	length = len(nums)
	max_num = max(nums)
	array = [0] * (max_num + 1)

	for num in nums:
		array[num] += 1

	count = (max_num + 1) - array.count(0)

	if count > length // 2:
		count = length // 2

	return count

print(solution([3, 3, 3, 2, 2, 4]))

print(solution([3, 3, 3, 2, 2, 2]))
