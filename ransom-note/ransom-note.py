class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        x = []
        for i in set(ransomNote):
            x.append(ransomNote.count(i) <= magazine.count(i))
            
        return all(x)
            