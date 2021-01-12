class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # one liner
        # return bin(int(a,2) + int(b,2))[2:]

        # 2nd approach
        carry = 0
        result = ''
        i = len(a) - 1
        j = len(b) - 1

        while (i >= 0 or j >= 0):
            sum = carry
            if i >= 0: sum+= ord(a[i]) - ord('0')
            if j >= 0: sum+= ord(b[j]) - ord('0')

            i -= 1
            j -= 1
            
            carry = 1 if sum > 1 else 0
            
            result += str(sum % 2)

        if carry != 0:
            result += str(carry)

        return result[::-1]

print(Solution().addBinary('11','1'))
print(Solution().addBinary('1010','1011'))

