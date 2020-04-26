class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'L':(0,-1), 'R':(0,1), 'U':(1,0), 'D':(-1,0)}
        pos = (0,0)
        for m in moves:
            r,c = d.get(m)
            r += pos[0]
            c += pos[1]
            pos = (r,c)
        return pos[0] == 0 and pos[1] == 0
