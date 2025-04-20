class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        count = 1
        length = len(nums)
        while j < length:
            if nums[i] == nums[j]:
                nums[j] = 101
            else:
                i = j
                count += 1
            j += 1
        nums.sort()
        return count
     
        