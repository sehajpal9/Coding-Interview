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
