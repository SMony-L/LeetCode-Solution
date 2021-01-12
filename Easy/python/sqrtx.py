class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        if x == 1: return 1
        left = 0
        right = x
        
        while left <= right:

            mid = left + (right - left) // 2
            
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid
            else:
                left = mid
                

print(Solution().mySqrt(4))       
print(Solution().mySqrt(16)) 
print(Solution().mySqrt(50))
print(Solution().mySqrt(100))
