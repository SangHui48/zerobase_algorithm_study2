# def solution(s):
#     if len(s) % 2 == 1:
#         return 0
#     if len(s) == 2:
#         return 1 if s[0] == s[1] else 0
#     target = ''
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             target = s.replace(s[i]*2, '')
#     if len(target) != 0:
#         if target[0] * 2 == target:
#             return 1
#     return 0

def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) > 0:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    return 1 if len(stack) == 0 else 0


print(solution('baabaa'))
# print(solution('cdcd'))