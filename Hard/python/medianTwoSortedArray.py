import unittest
from typing import List
from numpy import median
import statistics

class Solution:

    # 1st solution using libs
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     mergedList = nums1 + nums2
    #     # return median(mergedList)
    #     return statistics.median(mergedList)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0.0
        mergedList = sorted(nums1 + nums2)
        n = len(mergedList)
        index = n // 2

        if n % 2 == 0:
            result = (mergedList[(n -1)// 2] + mergedList[(n+1)//2] ) / 2
        else:
            result = mergedList[index]
        return result

class Test(unittest.TestCase):
    trueArr = [
        ([1,3],[2],2),
        ([1,2],[3,4],2.5),
        ([0,0],[0,0],0),
        ([],[1],1.0),
        ([2],[],2.0),
        ([1,2,3,4,5,6,7,8,9,10,12,13],[14,15,16,17,18,19,20],10.00000)
    ]


    def testEqualMedian(self):
        for [firstArr, secondArr, expectedMed] in self.trueArr:
            actual = Solution().findMedianSortedArrays(firstArr,secondArr)
            self.assertEqual(actual,expectedMed)

if __name__ == '__main__':
    unittest.main()