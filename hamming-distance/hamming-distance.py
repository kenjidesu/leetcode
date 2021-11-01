class Solution(object):
    def hammingDistance(self, x, y):
        # Get binary value
        bx = bin(x)[2:]
        by = bin(y)[2:]
        
        # Add 0 to match the value
        ls = abs(len(bx) - len(by))
        if ls:
            dd = '0' * ls
            if len(bx) > len(by):
                by = dd + by
            else:
                bx = dd + bx
        
        return sum(xi != yi for xi, yi in zip(bx, by))
            
                
            
        
        
        