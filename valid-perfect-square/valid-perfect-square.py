class Solution(object):
    def isPerfectSquare(self, num):
        odd = 1
        # we get the square root of num by subtracting it to odd numbers
        while num > 0:
            num -= odd
            # If num becomes negative that means it's not perfect square
            if num < 0:
                return False
            # We add 2 to odd because that's how odd number works
            odd += 2
            
        return True
            
        
        