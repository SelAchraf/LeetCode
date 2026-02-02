class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums_inferieure = [num for num in nums if num < target]
        maximum = max(nums_inferieure) if nums_inferieure else None
        
        for i in range (len(nums)):
            if nums[i] == target:
                return i
        
        index = nums.index(maximum)+1 if maximum else 0
        return index

solution = Solution()
nums = [1,3,5,6]
target = 2
result = solution.searchInsert(nums, target)
print(result)