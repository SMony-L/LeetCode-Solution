class Solution():
    def removeKdigits(self, nums: str, k: int) -> str:
        # Using stack
        n = len(nums)
        myStack = []
        for i in nums:
            # if k > 0 and stack is not empty and top of the stack is greater than i
            while (k > 0) and len(myStack) > 0 and myStack[-1] > i:
                myStack.pop()
                k-=1
            myStack.append(i) 

        if k > 0:
            myStack = myStack[:-k]   
        if len(myStack) == 0:
            return '0'   
        return ''.join(myStack).lstrip('0') or '0'

print(Solution().removeKdigits('1432219',3))
print(Solution().removeKdigits('1234',2))
print(Solution().removeKdigits('1001',2))
print(Solution().removeKdigits('10',2))
print(Solution().removeKdigits('10200',1))