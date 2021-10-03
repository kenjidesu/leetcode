class Solution(object):
    def wordPattern(self, pattern, s):
        # if length are not equal, there's definitely
        # something missing, so its False
        if len(pattern) != len(s.split()):
            return False
        
        # HashMap
        hmap = {}
        for i, j in enumerate(s.split()):
            if pattern[i] in hmap:
                # if the values is not equal to j, False
                if hmap[pattern[i]] != j:
                    return False
            # it makes sure the j is not in hmap
            elif j in hmap.values():
                return False
            # adds to hmap
            else:
                hmap[pattern[i]] = j
                
        return True
                
        