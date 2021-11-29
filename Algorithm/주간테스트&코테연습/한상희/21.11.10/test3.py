def solution(n):
    answer = 0
    data = list(str(n))
    for item in data:
        answer += int(item)
    return answer

print(solution(123))
print(solution(987))