#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) 
    {
        int i;
        for (i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                return i;
            }
            else if (nums[i] > target) {
                return i;
            }
        }
        return i;
    }
};

int main() {
    vector<int> arr {1,3,5,6};
    int target = 7;
    cout << Solution().searchInsert(arr, target) << endl;

}