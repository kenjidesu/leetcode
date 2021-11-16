class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5: return False
        
        fv, tn = 0, 0
        for i in bills:
            if i == 5:
                fv += 1
            elif i == 10:
                tn += 1
                fv -= 1
            else:
                if tn > 0:
                    tn -= 1
                    fv -= 1
                else:
                    fv -= 3
            
            if fv < 0: return False
            
        return True
        