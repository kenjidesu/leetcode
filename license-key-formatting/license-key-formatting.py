class Solution(object):
    def licenseKeyFormatting(self, s, k):
        st = ""
        c = 0
        for i in reversed(s):
            # Only Alphanumeric characters
            if i.isalnum():
                # Add dash if group contains k characters
                if c == k:
                    st += '-'
                    c = 0
                st += i
                # Tracks how many char in current group
                c += 1
        
        # Return the reversed st.uppercase()
        return st[::-1].upper()
        