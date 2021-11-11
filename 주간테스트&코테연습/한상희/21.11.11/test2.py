from collections import deque
INF = 9999999 #500000이상 중 가장 큰 수

def bfs(start_node, graph, N, K):
    queue = deque([start_node])
    #저장, 초기비용 max로 초기화
    table = [INF] * (N + 1)
    #출발점 비용 0
    table[1] = 0

    while queue:
        node = queue.popleft()
        start = node[0]
        cost = node[1]
        for ar_info in graph[start]:
            arrive, d_cost = ar_info[0], ar_info[1]
            if cost + d_cost <= K and cost + d_cost <= table[arrive]:
                table[arrive] = cost + d_cost
                queue.append([arrive, cost + d_cost])
    return table

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for info in road: # 0: 출발  1: 도착  2: 비용
        graph[info[0]].append((info[1], info[2]))
        graph[info[1]].append((info[0], info[2]))

    results = bfs([1, 0], graph, N, K)

    for result in results:
        if result != INF:
            answer += 1
    return answer

# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))