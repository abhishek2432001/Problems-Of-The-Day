'''Complement
You are given a binary string str. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and complement the characters between L and R i.e strL, strL+1, …, strR. By complement, we mean change character 0 to 1 and vice-versa.

You task is to perform ATMOST one operation such that in final string number of 1s is maximised. If there is no need to completement, i.e., string contains all 1s, return -1. Else, return the two values denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Example 1:

Input:
N = 3
str = "111"
Output: -1
Explanation: As all characters are '1', 
so don't need to complement any.

Example 2:

Input:
N = 2
str = "01"
Output: 1 1
Explanation: After complementing [1, 1] 
the string becomes "11".'''

def findRange(a, size):
	arr = [1 if i == '0' else -1 for i in a]
	
	l, r, res = 0, 0,[0, 0]
	
	cursum, maxsum = 0, float('-inf')
	
	for i in range(len(arr)):
	    if arr[i] > arr[i] + cursum:
	        l = i
	        cursum = arr[i]
	        
	    else:
	        cursum = arr[i] + cursum
	        
	    r = i
	    if cursum > maxsum:
	        maxsum = cursum
	        res = [l + 1, r + 1]
	        
	return res if maxsum >= 0 else [-1]
