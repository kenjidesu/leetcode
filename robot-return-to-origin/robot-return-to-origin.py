class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')
        