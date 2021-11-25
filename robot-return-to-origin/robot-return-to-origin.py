class Solution(object):
    def judgeCircle(self, moves):
        # Track its moves
        x = 0
        y = 0
        for i in range(len(moves)):
            # Add 1 if Up or Right, -1 if Left or Down
            if moves[i] == 'U':
                x += 1
            elif moves[i] == 'D':
                x -= 1
            elif moves[i] == 'R':
                y += 1
            elif moves[i] == 'L':
                y -= 1
        
        # True if x and y == 0 else False
        return x == 0 and y == 0