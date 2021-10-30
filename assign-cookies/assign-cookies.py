class Solution(object):
    def findContentChildren(self, g, s):
        """
        We sorted the g, s first so we can do a Two Pointer Approach because if we 
        did not sort it and g happens to be [3, 2, 1] and s = [1, 1], we can't
        satisfy the g[0] since we only have 1 cookie at s[i] and the output for
        this input will be 0.
        
        Code below uses a Two Pointer approach, when j (which is the cookie) satisfy
        the i (which is the child), we move to the next i and j, but if j can't satisfy
        i we move j for the bigger cookie since our s are already sorted and we know that
        the next j is bigger than the previous j and also i wants more j.
        
        In the end, we return how many children are satisfied with the cookies they
        received
        """
        # Sort g, s
        g.sort()
        s.sort()
        
        # Two pointer Approach
        i, j = 0, 0;
        while i < len(g) and j < len(s): 
            if g[i] <= s[j]:
                # Move both pointer to next one
                i += 1
                j += 1
            else:
                # Only move j pointer to next one
                j += 1
                
        return i