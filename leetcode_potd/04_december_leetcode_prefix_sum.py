import math
# Make prefix and suffix array
def minimumAverageDifference(nums) -> int:
        mini = float('inf')
        res = [0,mini]
        tot = sum(nums)
        n = len(nums)
        pre = 0
        
        for i in range(n-1):
            pre += nums[i]
            avgdiff = abs(math.floor(pre/(i+1))-math.floor((tot-pre)/(n-i-1)))
            if(avgdiff<res[1]):
                res[0] = i
                res[1] = avgdiff
        last_diff = tot//n
        if last_diff<res[1]:
            res[0] = n-1
        return res[0]
nums = [2,5,3,9,5,3]
print(minimumAverageDifference(nums))