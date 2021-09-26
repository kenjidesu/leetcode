class Solution(object):
    def reverseVowels(self, s):
        # gets all the vowels
        v = []
        for i in s:
            if lower(i) in 'aeiou':
                v.append(i)
        
        # updates the string
        r = [i for i in s]
        for j in range(len(r)):
            if lower(r[j]) in 'aeiou':
                # pop(), gets the last vowel
                r[j] = v.pop()
            
        # return the updated string
        return "".join(c for c in r)
        
        
            
                
        