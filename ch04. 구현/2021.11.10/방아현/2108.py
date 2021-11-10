from collections import Counter
import sys

input = sys.stdin.readline

numbers = []
for _ in range(int(input())):
	numbers.append(int(input()))

numbers.sort()

# 산술평균
print(round(sum(numbers) / len(numbers)))
# 중앙값
print(numbers[len(numbers) // 2])
# 최빈값
cnt = Counter(numbers).most_common(2) #최빈값 중에서 두번째로 작은값을 출력하기 위해서 # most_common에서 갯수가 같을 경우에는 먼저 만난 순서대로 출력된다.
if len(numbers) > 1:
	if cnt[0][1] == cnt[1][1]: # sort()를 한 번 했기 때문에 most_common에서 먼저 만난 앞의 숫자가 무조건 작다.
		print(cnt[1][0])
	else:
		print(cnt[0][0])
else:
	print(numbers[0])
# 범위
print(max(numbers) - min(numbers))

