class Solution(object):
    def licenseKeyFormatting(self, s, k):        
        nd = [i for i in s if i.isalnum()]
        st = ""
        c = 0
        for i in reversed(nd):
            if c == k:
                st += '-'
                c = 0
            st += i
            c += 1
                    
        return st.upper()[::-1]
        