#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        // Slow solution
        // int i = 1;
        // while (i < nums.size()) {
        //     if (nums[i] == nums[i-1]) {
        //         nums.erase(nums.begin() + i);
        //     } else {
        //         i++;
        //     }
        // }
        // return nums.size();

        // Two Pointers
        if (nums.size() <= 1) {
            return nums.size();
        }
        int curr = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[curr]) {
                nums[++curr] = nums[i];
            }
        }
        return curr + 1; 
    }
};

int main() {
    vector<int> arr {0,0,1,1,1,2,2,3,3,4}; 
    // vector<int> arr{1,1,2};
    int result = Solution().removeDuplicates(arr);
    cout << result << endl;
    return 0;
}