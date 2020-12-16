from typing import List

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        # n = (sum(A) - sum(B)) // 2
        # A = list(map(lambda a: a - n, A))
        # b = (list(set(A) & set(B)))[0]
        # return [b + n, b]


        dif = (sum(A) - sum(B)) // 2
        for i in set(B):
            if dif + i in set(A):
                return [dif + i, i]
        
print(Solution().fairCandySwap([1,1],[2,2]))
print(Solution().fairCandySwap([1,2],[2,3]))
print(Solution().fairCandySwap([2],[1,3]))
print(Solution().fairCandySwap([1,2,5],[2,4]))
print(Solution().fairCandySwap([35,17,4,24,10],[63,21]))
