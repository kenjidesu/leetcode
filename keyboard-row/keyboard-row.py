class Solution(object):
    def findWords(self, words):
        x = "qwertyuiop"    # 1st row of kb chars
        y = "asdfghjkl"     # 2nd row of kb chars
        z = "zxcvbnm"       # 3rd row of kb chars
        arr = []            # return array
        # loop through given words
        for i in words:
            # false if some char is not in kb chars, otherwise true
            x_bol = 0 not in [c in x for c in set(i.lower())]
            y_bol = 0 not in [c in y for c in set(i.lower())]
            z_bol = 0 not in [c in z for c in set(i.lower())]
            # any(), returns True if any of the elements of a given iterable
            # are True else it returns False
            if any([x_bol, y_bol, z_bol]):
                # appends if some of xyz bol's are true
                arr.append(i)
        
        return arr
        