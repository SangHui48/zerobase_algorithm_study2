def solution(n,a,b):
    answer = 0
    while True:
        if a == b:
            break
        a, b = (a+1) // 2, (b+1) // 2
        answer += 1
    return answer

print(solution(8, 4, 7))