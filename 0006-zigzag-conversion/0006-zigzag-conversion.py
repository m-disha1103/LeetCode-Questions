class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move row pointer
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        return "".join(rows)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        