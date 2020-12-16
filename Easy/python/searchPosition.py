from typing import List
import unittest
class Solution():
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1st approach

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif target not in nums:
        #         nums.append(target)
        #         nums.sort()
        #         return nums.index(target)

        # 2nd approach (Binary Search)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left  = mid + 1
        return left

class Test(unittest.TestCase):
    array1 = [
        ([1,3,5,6],5,2),
        ([1,3,5,6],2,1),
        ([1,3,5,6],7,4),
        ([1,3,5,6],0,0),
        ([1],0,0)]
    
    def testSearchInsert(self):
        
        for [testArr, testTarget, expected] in self.array1:
            actual = Solution().searchInsert(testArr,testTarget)
            self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()