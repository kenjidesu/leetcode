class Solution(object):
    def wordPattern(self, pattern, s):
        if len(pattern) != len(s.split()):
            return False
        
        hmap = {}
        for i, j in enumerate(s.split()):
            if pattern[i] in hmap:
                if hmap[pattern[i]] != j:
                    return False
            elif j in hmap.values():
                return False
            else:
                hmap[pattern[i]] = j
                
        return True
                
        