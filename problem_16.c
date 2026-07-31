#include <stdlib.h>

int absVal(int x) {
    return x < 0 ? -x : x;
}

int threeSumClosest(int* nums, int numsSize, int target) {
    int best = nums[0] + nums[1] + nums[2];

    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            for (int k = j + 1; k < numsSize; k++) {
                int sum = nums[i] + nums[j] + nums[k];

                if (absVal(sum - target) < absVal(best - target)) {
                    best = sum;
                }
            }
        }
    }

    return best;
}