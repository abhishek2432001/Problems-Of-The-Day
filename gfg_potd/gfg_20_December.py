'''A difference of values and indexes

Given an unsorted array arr[ ] of size n, you need to find the maximum difference of absolute values of elements and indexes, i.e., for i <= j, calculate maximum of | arr[ i ] - arr[ j ] | + | i - j |. 

Example 1:

Input : 
n = 3
arr[ ] = {1, 3, -1}
Output: 5
Explanation:
Maximum difference comes from indexes 
1, 2 i.e | 3 - (-1) | + | 1 - 2 | = 5

Example 2:

Input : 
n = 4
arr[ ] = {5, 9, 2, 6} 
Output:  8
Explanation: 
Maximum difference comes from indexes 
1, 2 i.e | 9 - 2 | + | 1 - 2 | = 8'''

class Solution:
    def maxDistance (self, arr, n) : 
        max1,min1=-9999999,999999

        max2,min2=-9999999,999999

        for i in range(n):

            max1=max(max1,arr[i]+i)

            max2=max(max2,arr[i]-i)

            min1=min(min1,arr[i]+i)

            min2=min(min2,arr[i]-i)

            a=max(max1-min1,max2-min2)

        return a





