#sort by parity

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        return [k for k in A if k %2==0] + [k for k in A if k %2==1]
