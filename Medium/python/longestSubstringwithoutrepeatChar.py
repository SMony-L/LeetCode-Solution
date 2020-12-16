# Given a string s, find the length of the longest substring without repeating characters.
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if (len(s) == 0): return 0
        # maxCount = 0
        # newList = []
        # for i in range(len(s)-1):
        #     newList.append(s[i])
        #     for j in range(i+1, len(s)):
        #         if s[j] not in newList:
        #             newList.append(s[j])
        #         else:
        #             if (len(newList) > maxCount):
        #                 maxCount = len(newList)
        #             break

        #     if (len(newList) > maxCount):
        #         maxCount = len(newList)
        #     newList = []
        # return maxCount
        myDict = {}
        result = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in myDict:
                myDict[s[i]] = i
            else:
                j = max(j, myDict[s[i]]+ 1)
                myDict[s[i]] = i

            result = max(result, i - j + 1)
        return result


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