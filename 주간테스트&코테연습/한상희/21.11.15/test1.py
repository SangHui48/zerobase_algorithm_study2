# def solution(no, works):
#     if no > sum(works):
#         return 0
#     result = 0
#     while no > 0:
#         # 매순간 가장 많이 남은 작업 찾기
#         works.sort()
#         works[-1] -= 1
#         no -= 1
#     for work in works:
#         result += work ** 2
#     return result

import heapq

def solution(no, works):
    if no > sum(works):
        return 0
    schedule = [-i for i in works]
    heapq.heapify(schedule)
    while no > 0:
        tmp = heapq.heappop(schedule)
        tmp += 1
        heapq.heappush(schedule, tmp)
        no -= 1
    return sum([i ** 2 for i in schedule])

print(solution(4, [4,3,3]))
print(solution(2, [3,3,3]))