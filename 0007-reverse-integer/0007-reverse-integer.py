class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        rev = 0
        y = abs(x)
        
        while y != 0:
            if rev * 10 + (y % 10) <= 2**31:
                rev = rev * 10 + (y % 10)
                y = y // 10
            else:
                return 0
        
        if x > 0:
            return rev
        else:
            return -rev