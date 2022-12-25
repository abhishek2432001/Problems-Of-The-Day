'''Missing number in matrix
Given a matrix of size n x n such that it has only one 0, Find the positive number (greater than zero) to be placed in place of the 0 such that sum of the numbers in every row, column and two diagonals become equal. If no such number exists, return -1.
Note: Diagonals should be only of the form matrix[i][i] and matrix[i][n-i-1]. n is always greater than 1.
Example 1:
Input: matrix = {{5, 5}, {5, 0}}
Output: 5
Explanation: The matrix is
5 5
5 0
Therefore If we place 5 instead of 0, all
the element of matrix will become 5. 
Therefore row 5+5=10, column 5+5=10 and 
diagonal 5+5=10, all are equal.
Example 2:
Input: matrix = {{1, 2, 0}, {3, 1, 2}, 
{2, 3, 1}}
Output: -1
Explanation: It is not possible to insert 
an element in place of 0 so that the 
condition is satisfied.thus result is -1. '''
#User function Template for python3

def isValid(matrix, s):
    n = len(matrix)
    if not all(sum([matrix[i][j] for j in range(n)]) == s for i in range(n)):
        return False
    elif not all(sum([matrix[i][j] for i in range(n)]) == s for j in range(n)):
        return False
    elif sum([matrix[i][i] for i in range(n)]) != s:
        return False
    elif sum([matrix[i][n-i-1] for i in range(n)]) != s:
        return False
    return True

def MissingNo(matrix):
    n = len(matrix)
    zx, zy = None, None
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                zx, zy = i, j
    nx = (zx + 1)%n
    s, sx = sum(matrix[nx]), sum(matrix[zx])
    matrix[zx][zy] = s - sx
    return matrix[zx][zy] if matrix[zx][zy]>0 and self.isValid(matrix, s) else -1
