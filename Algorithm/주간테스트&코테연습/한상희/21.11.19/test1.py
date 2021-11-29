def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_idx, b_idx = 0, 0
    while True:
        if b_idx == len(B):
            break
        if B[b_idx] > A[a_idx]:
            answer += 1
            b_idx += 1
            a_idx += 1
        else:
            b_idx += 1
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))