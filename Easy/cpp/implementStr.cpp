#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) {return 0;}
        if (needle.length() > haystack.length()) {return -1;}
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            int j;
            for (j = 0; j < needle.length(); j++) {
                if (haystack[i+j] != needle[j]) {
                    break;
                }
            }
            if (j == needle.length()) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    string hay = "hello"; 
    string need = "ll";
    int result = Solution().strStr(hay,need);
    cout << result << endl;
    return 0;
}