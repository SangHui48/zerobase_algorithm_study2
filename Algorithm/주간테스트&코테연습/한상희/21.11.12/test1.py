def solution(v):
    answer = []
    x = [item[0] for item in v]
    y = [item[1] for item in v]
    for i in x:
        if x.count(i) == 1:
            answer.append(i)
    for j in y:
        if y.count(j) == 1:
            answer.append(j)
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))