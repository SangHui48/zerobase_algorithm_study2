from collections import deque

n, k = map(int, input().split())

q = deque([])

for i in range(1, n + 1):
	q.append(i)

print("<", end='')
while q:
	for _ in range(k - 1):
		q.append(q.popleft())
	if len(q) == 1:
		print(q.popleft(), end="")
	else:
		print(q.popleft(), end=', ')
print(">")
