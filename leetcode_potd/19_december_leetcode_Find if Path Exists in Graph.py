'''There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [False]*n
        d = {}
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
                
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]
        q = [start]
        while q:
            curr = q.pop(0)  
            if curr == end:  
                return True
            elif curr in d and not visited[curr]: 
                q.extend(d[curr])  
            visited[curr] = True  
        return False