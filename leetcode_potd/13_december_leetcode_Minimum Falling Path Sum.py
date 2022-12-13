'''Minimum Falling Path Sum
3.4K
103
Companies
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.'''

def minFallingPathSum(cost):
    R,C=len(cost),len(cost)
    tc = [[float('inf') for x in range(C)] for x in range(R)]
    tc[0][0] = cost[0][0] 
    for j in range(1, R): 
        tc[0][j] = cost[0][j] 
    for i in range(1,R): 
        for j in range(R):
            if i>0 and j>0:
                tc[i][j] = tc[i-1][j-1]
            if i>0:
                tc[i][j]=min(tc[i][j],tc[i-1][j])
            if j<R-1 and i>0:
                tc[i][j]=min(tc[i][j],tc[i-1][j+1])
            tc[i][j]+=cost[i][j] 
    # print tc
    return min(tc[-1])