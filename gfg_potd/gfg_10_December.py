'''Given a number k and string num of digits (0 to 9) denoting a positive integer. 
Find a string denoting the lowest integer number possible by removing k digits from num,
 without changing their order.
Note: num will not contain any leading zero.
Example 1:

Input:
k = 2
num = "143729"
Output: "1329"
Explanation: 1329 is the minimum number
possible after removing '4' and '7'.'''

def buildLowestNumber(S,N):
    stack = []
    
    for num in S:
        while N and stack and stack[-1] > num:
            stack.pop()
            N -= 1
            
        stack.append(num)
        
    final = ''.join(stack[:len(stack) - N]).lstrip('0')
    
    return "0" if not final else final