class Solution(object):
    def removeElement(self, nums, val):
       length = len(nums)
       count = 0
       for i in nums[:]:
           if i == val:
               nums.remove(i)
               count += 1
       k = length - count
       return k

            
        