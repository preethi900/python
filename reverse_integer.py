#Reverse integer program


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        inputnumber = str(x)
        # Reverse answer
        if "-" in inputnumber:
           ans =  int(inputnumber[0] + inputnumber[1:][::-1])
        else:
           ans = int(inputnumber[::-1])
        
        # Handle the 32 bit signed integer condition
        if ans > (2**31-1) or ans < -(2**31):
            return 0
        else:
            return ans
        
