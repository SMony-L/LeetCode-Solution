#include <map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            map<int, int> hash;

            for (int i = 0; i < nums.size(); i++) 
            {
            int numberToFind = target - nums[i];

            if (hash.find(numberToFind) != hash.end()) 
                return  {hash[numberToFind] ,i };

                hash[nums[i]] = i;
            }
            return {};
        }
        
};
