#add digits

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))==1:
            return num
        else:
            a = [int(x) for x in str(num)]
            return self.addDigits(sum(a))
