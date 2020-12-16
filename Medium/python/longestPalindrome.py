import unittest

class Solution():
    def longestPalindrome(self, s:str) -> str:
        # edge case if string is not empty
        if len(s) == 1: return s

        # two pointers approach
        # get substrings
        subStringList = []
        longestSubPal = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # check for palinedrome
                if s[i:j] == s[i:j][::-1]:
                    # check length
                    if len(s[i:j]) > len(longestSubPal):
                        longestSubPal = s[i:j]
        return longestSubPal

class Test(unittest.TestCase):
    string1 = [
        ('babad','bab'),
        ('cbbd','bb'),
        ('a','a'),
        ('ac','a'),
        ('qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj','gjjg')]
    def testLongestPalindrome(self):
        for testString, expected in self.string1:
            actual = Solution().longestPalindrome(testString)
            self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()