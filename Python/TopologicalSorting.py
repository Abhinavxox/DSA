#topological sorting
def ancestors(n, edgeList):
    adj_list = {i: [] for i in range(n)}
    indegree = [0] * n
    for u, v in edgeList:
        adj_list[u].append(v)
        indegree[v] += 1
    # print(indegree)
    # print(adj_list)

    queue = [i for i in range(n) if indegree[i] == 0]
    # print(queue)
    result = [[] for _ in range(n)]
    while queue:
        node = queue.pop(0)
        for neighbor in adj_list[node]:
            result[neighbor] += result[node] + [node]
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return [sorted(x) for x in result]

print(ancestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))