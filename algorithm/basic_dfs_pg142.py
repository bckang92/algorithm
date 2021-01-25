import time

def dfs(graph, v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            print(i, '로가')
            dfs(graph, i, visited)

#하나 쭉 타고 재귀재귀재귀 가다 끝을 봐야 중간에 안간데서 다음재귀 콜

#2차원 리스트
graph = [
    [],
    [2, 3, 8], #1
    [1, 7], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2, 6, 8], #7
    [1, 7] #8
]

#각 노드가 방문된 정보를 리스트로 표현
visited = [False] * 9

dfs(graph, 1, visited)

