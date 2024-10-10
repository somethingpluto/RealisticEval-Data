#include <iostream>
#include <vector>
#include <algorithm>

int minRemovalsToMakeUnique(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());
    int count = 0;
    for(int i = 1; i < nums.size(); ++i){
        if(nums[i] <= nums[i-1]){
            int diff = nums[i-1] - nums[i];
            nums[i] += diff + 1;
            count += diff + 1;
        }
    }
    return count;
}