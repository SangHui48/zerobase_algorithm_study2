def solution(arr):
    answer = []
    tmp = 0
    for i in range(len(arr)):
        if i == 0:
            tmp = arr[i]
            answer.append(arr[i])
        else:
            if tmp != arr[i]:
                answer.append(arr[i])
            tmp = arr[i]
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))