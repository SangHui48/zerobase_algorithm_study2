def solution(arr):
    answer = True
    arr.sort()
    if arr[0] != 1:
        return False
    for i in range(len(arr)-1):
        if arr[i + 1] != arr[i] + 1:
            return False
    return answer

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))