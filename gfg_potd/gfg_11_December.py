'''Given an array of integers and a number k, write a function that returns true if 
given array can be divided into pairs such that sum of every pair is divisible by k.
Example 1 :

Input : arr = [9, 5, 7, 3], k = 6
Output: True
Explanation: {(9, 3), (5, 7)} is a 
possible solution. 9 + 3 = 12 is divisible
by 6 and 7 + 5 = 12 is also divisible by 6.
'''
def canPair(nums, k):
		# Code here
	d={}

    for i in range(k):
        d[i]=0
    for i in range(0,n):
        d[nums[i]%k]+=1
    for i in d:
        if (i==(k-i) or i==0) and d[i]%2!=0 :
            return False
        elif i!=0 and d[i]!=d[k-i]:
             return False
    return True