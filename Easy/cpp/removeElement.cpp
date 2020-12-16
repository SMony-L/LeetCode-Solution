#include <iostream>
#include <vector>

using namespace std;


class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int curr = 0;
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] != val) {
                    nums[curr] = nums[i];
                    curr++;
                }
                cout << curr << endl;
            }
            return curr;
        }
};

int main() {
    vector<int> arr {3,2,2,3}; 
    int val = 3;
    int result = Solution().removeElement(arr,val);
    // cout << result << endl;
    return 0;

}