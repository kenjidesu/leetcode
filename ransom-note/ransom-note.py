class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # bool arr
        x = []
        for i in set(ransomNote):
            # append if ransomnote i is less than or equal to magazine i
            x.append(ransomNote.count(i) <= magazine.count(i))
            
        # if everything in x is True, returns True otherwise False
        return all(x)
            