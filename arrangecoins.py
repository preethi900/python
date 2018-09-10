#Arrange coins

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        
        while n >= 0:
            n -= k
            k += 1
            
        return k - 2
