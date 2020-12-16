from typing import List

class Solution:
    # O(N Log N)
    # Divide and Conquer
    # def maxSubArray(self, nums: List[int]) -> int:
    #     answer = self.dAc(nums, 0, len(nums) - 1)
    #     return answer
        
        
    # def dAc(self, nums, l, r):
    #     if l == r:
    #         return nums[l]

    #     mid = l + (r - l) // 2 # mid point
        
    #     leftMax = self.dAc(nums, l, mid) # first half
        
    #     rightMax = self.dAc(nums, mid + 1, r) # second half
        
    #     answer = 0
    #     left = float('-inf')
    #     right = float('-inf')
    
    #     # get the left side max
    #     for i in range(mid, l - 1, -1):
    #         answer += nums[i]
    #         left = max(left, answer)

    #     # get the right side max
    #     answer = 0
    #     for j in range(mid + 1, r + 1, 1):
    #         answer += nums[j]
    #         right = max(answer, right)
        
    #     return max(leftMax, rightMax, left + right)


    # Dynamic Programming
    # O(N)
    def maxSubArray(self, nums):
        maxNum, currSum = max(nums), 0
        for i in range(len(nums)):
            if currSum + nums[i] < 0:
                currSum = 0
            else:
                currSum, maxNum = currSum + nums[i], max(maxNum, currSum + nums[i])
        return maxNum
            
        

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([0]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([-2147483647]))