import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
	val = int(input())
	if val == 0:
		result.pop()
	else:
		result.append(val)

print(sum(result))
