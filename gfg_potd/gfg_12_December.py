def articulationPoints(V, adj):
    ap = [False]*V
    visited = [False]*V
    dis = [0]*V
    low = [float('inf')]*V 
    timer = 0
    def dfs(v, p=-1):
        nonlocal ap, visited, dis, low, timer
        visited[v] = True
        dis[v] = low[v] = timer
        timer += 1
        children = 0
        for to in adj[v]:
            if to == p: #go back to parent directly
                continue
            if visited[to]: # back-edge
                low[v] = min(low[v], dis[to])
            else:
                children += 1
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] >= dis[v] and p != -1:
                    ap[v] = True
        if p == -1 and children > 1:
            ap[v] = True
    for v in range(V):
        if not visited[v]:
            dfs(v)
    ap = [i for i, v in enumerate(ap) if v]
    return ap if ap else [-1]