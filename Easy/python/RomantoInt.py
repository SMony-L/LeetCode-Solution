class Solution:
    def romantoInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
        num, prev = 0,0
    
        for i in range(len(s)-1,-1,-1):
            init_val = roman[s[i]]
        
            if (init_val < prev):
                num -= roman[s[i]]
                
            else:
                num += roman[s[i]]
    
            prev = init_val
            
            
        return num


if __name__ == "__main__":
    S = Solution()
    print(S.romantoInt('XL'))

        