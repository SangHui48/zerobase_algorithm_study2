from itertools import combinations
def solution(nums):
    answer = 0
    all_case = list(combinations(nums, 3))
    for case in all_case:
        total = sum(case)
        for i in range(2, total+1):
            if i == total:
                answer += 1
            if total % i == 0:
                break
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))