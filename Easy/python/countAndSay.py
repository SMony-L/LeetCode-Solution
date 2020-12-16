class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n <= 1:
            return '1'
        s = '1'
        for i in range(n-1):
            previous, counter = s[0], 0
            finalString = ''
            for character in s:
                
                if previous != character:
                    finalString += str(counter) + previous
                    previous = character
                    counter = 1
                else:
                    counter += 1
            finalString += str(counter) + previous
            s = finalString
        return s

print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))