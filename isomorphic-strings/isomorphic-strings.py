class Solution(object):
    def isIsomorphic(self, s, t):
        # zip(), brings elements of the same index from 
        # multiple iterable objects together as elements of the same tuples
        z = zip(s, t)
        # gets the length of non-duplicated zz
        l = len(set(z))
        
        # checks whether the length of s,t == l
        return l == len(set(s)) == len(set(t))
        
        