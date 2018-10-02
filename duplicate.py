#find duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l1 = len(nums)
        l2 = len(set(nums))
        if l1 == l2:
            return False
        else:
            return True
