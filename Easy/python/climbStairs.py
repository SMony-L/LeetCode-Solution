class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))