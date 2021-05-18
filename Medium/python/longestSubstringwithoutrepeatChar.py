# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import unittest

class Solution:
    # 1st solution
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     myDictionary = {}
    #     maxLength = 0
    #     ans = 0
        
    #     for i in range(len(s)):
    #         if s[i] not in myDictionary:
    #             myDictionary[s[i]] = i
                
    #         else:
            
    #             maxLength = max(maxLength, myDictionary[s[i]] + 1)
    #             myDictionary[s[i]] = i
                
    #         ans = max(ans, i - maxLength + 1)
    #     return ans

    # 2nd solution
    # def lengthOfLongestSubstring(self, s:str) -> int:
    #     seen = ''
    #     mx = 0
    #     for c in s:
    #         if c not in seen:
    #             seen+=c
    #         else:
    #             seen = seen[seen.index(c) + 1:] + c
    #         mx = max(mx, len(seen))
    #     return mx

    # 3rd solution
    def lengthOfLongestSubstring(self, s:str) -> int:
        seen = ''
        maxLength = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen += s[i]
            else:
                seen = seen[seen.index(s[i]) + 1:] + s[i]
            maxLength = max(maxLength, len(seen))
        return maxLength

class Test(unittest.TestCase):
    string1 = [('abcabcbb', 3), ('abc',3), ('pwwkew',3)]
    string2 = [('bbbb',3), ("",3) ,('abcde',3)]

    # Equal 3 
    def testEqualLongestSub(self):
        for testString, secondString in self.string1:
            result = Solution()
            actual = result.lengthOfLongestSubstring(testString)
            self.assertEqual(actual,secondString,"Equal")
    # Not Equal 3
    def testNotEqualLongestSub(self):
        for testString, secondString in self.string2:
            result = Solution()
            actual = result.lengthOfLongestSubstring(testString)
            self.assertNotEqual(actual,secondString,"Not Equal")


if __name__ == '__main__':
    unittest.main()