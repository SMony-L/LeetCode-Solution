#include <string>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            
            if (strs.size() == 0) {return "";} 
            if (strs.size() == 1) {return strs[0];}
            for (int i = 0; ; i++) {
                for (auto &s: strs) {
                    if(i >= s.size() || s[i] != strs[0][i]){
                        return strs[0].substr(0,i);
                    }
                }
            }
            return "";
        }
};

int main() {   
    // vector<string> words { "flower", "flow", "flight"};
    vector<string> words {"flower", "flower", "flower", "flower"};
    Solution result;
    cout << result.longestCommonPrefix(words) << endl;

    return 0;
}