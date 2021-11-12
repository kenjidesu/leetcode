class Solution(object):
    def finalValueAfterOperations(self, operations):
        # return 0 if there's no operation
        if len(operations) == 0: return 0
        
        n = 0
        for i in operations:
            if '-' in i:
                n -= 1
            elif '+' in i:
                n += 1
                
        return n
        