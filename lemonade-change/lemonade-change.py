class Solution(object):
    def lemonadeChange(self, bills):
        # We have no change for bills >= 10
        if bills[0] != 5: return False
        
        # We don't need to track $20 cus we can't use it
        # for giving change
        fv, tn = 0, 0
        for i in bills:
            if i == 5:
                fv += 1
            # We deduct $5 to $10 for everytime we receive $10
            elif i == 10:
                tn += 1
                fv -= 1
            else:
                # Deduct $10 and $5 everytime we recieve $20
                if tn > 0:
                    tn -= 1
                    fv -= 1
                # If tn is 0, deduct three $5
                else:
                    fv -= 3
            # If fv becomes negative, we don't have change anymore           
            if fv < 0: return False
            
        return True
        