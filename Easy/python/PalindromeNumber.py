class Solution:
    def isPalinedrome(self, x:int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    S = Solution()
    if(S.isPalinedrome(101)):
        print("Yes")
    else:
        print("No")