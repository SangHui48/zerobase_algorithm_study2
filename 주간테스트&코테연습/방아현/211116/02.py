def solution(s):
	s = list(s)
	arr = [s[0],]
	for i in range(1, len(s)):
		if arr:
			if s[i] == arr[-1]:
				arr.pop()
			else:
				arr.append(s[i])
		else:
			arr.append(s[i])
	if arr:
		return 0
	else:
		return 1

print(solution("baabaa"))
print(solution("cdcd"))
