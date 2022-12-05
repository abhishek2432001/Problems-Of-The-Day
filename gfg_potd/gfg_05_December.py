'''Given a 2-D binary matrix of size n*m, where 0 represents an empty space while 1 represents a 
wall you cannot walk through. You are also given an integer k.You can walk up, down, left, or right.
Given that you can remove up to k walls, return the minimum number of steps to walk from the 
top left corner (0, 0) to the bottom right corner (n-1, m-1).
Note: If there is no way to walk from the top left corner to the bottom right corner, return -1.

Example 1:

Input: n = 3, m = 3, k = 1
mat = {{0, 0, 0},
       {0, 0, 1},
       {0, 1, 0}}
Output:
4
Explanation:
We can remove any one of the walls and
reach the bottom in 4 moves.'''

def shotestPath(self, grid, n, m, k):
    start = (0, 0, k)
    q = [start]
    visited = {(0, 0): k}
    
    steps = 0
    while q:
        nq = []
        for r0, c0, k0 in q:
            if r0 == n-1 and c0 == m-1:
                return steps
                
            nk = k0-grid[r0][c0]
            if nk < 0:
                continue
            
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                r = r0+dr
                c = c0+dc
                if r < 0 or r >= n or c < 0 or c >= m:
                    continue
                if (r,c) not in visited or visited[r, c] < nk:
                    visited[r, c] = nk
                    nq.append((r, c, nk))
        steps += 1
        q = nq
    return -1