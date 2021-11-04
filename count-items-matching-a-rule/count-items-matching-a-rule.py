class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        # counter of the match rule
        rt = 0
        
        # checks the ruleKey and set it to their ith place
        if ruleKey == "type":
            x = 0
        elif ruleKey == "color":
            x = 1
        else:
            x = 2
        
        # checks every xth place of each item
        for i in range(len(items)):
            # increment one if match
            if items[i][x] == ruleValue:
                rt += 1
                
        return rt
        