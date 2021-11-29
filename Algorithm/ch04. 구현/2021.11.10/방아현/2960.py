import sys
input = sys.stdin.readline

n, k = map(int,input().split())
array = [1] * (n + 1)

count = 0
flag = False
for i in range(2, n + 1):
	if array[i] == 1:
		for j in range(i, n + 1, i):
			if array[j] == 1:
				count += 1
				array[j] = 0
				if count == k:
					print(j)
					flag = True
					break
		if flag:
			break
