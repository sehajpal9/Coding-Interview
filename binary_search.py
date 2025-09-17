# binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2  # integer mid
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1         # shrink right half
            else:
                left = middle + 1          # shrink left half

        return -1
