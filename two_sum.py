# given an array, return the two consecutive numbers whose sum equals the given target 
# example: nums = [1,2,3,4], target = 7, output = [2,3] because nums[2]->3 + nums[3]->4 = 7

def two_sum(nums, target):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    indices.append(i)
                    indices.append(j)
                    return indices

        return indices


# two sum case for NON consecutive numbers
def twoSum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # found the pair
            return [seen[complement], i]
        # store the current number in the map
        seen[num] = i

    return []  # if no solution (though problem guarantees one)
