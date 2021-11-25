class Solution(object):
    def calPoints(self, ops):
        pp = []
        for i in ops:
            # sum previous two scores
            if i == '+':
                pp.append(pp[-2] + pp[-1])
            # double the previous score
            elif i == 'D':
                pp.append(pp[-1] * 2)
            # invalidate the previous score
            elif i == 'C':
                pp.pop()
            # append int(i)
            else:
                pp.append(int(i))
                
        return sum(pp)
        