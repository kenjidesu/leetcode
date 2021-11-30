from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        val = Counter(deck).values()
        return gcd(*val) >= 2