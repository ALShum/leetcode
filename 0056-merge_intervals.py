## Sort intervals
## Merge by checking for overlap: does left point fall into range of the previous interval

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted([tuple(i) for i in intervals])

        ivals = []
        p_l, p_r = intervals[0]
        for i in range(1, len(intervals)):
            c_l, c_r = intervals[i]

            if p_l <= c_l <= p_r:
                p_l = p_l
                p_r = max(p_r, c_r)
            else:
                ivals.append((p_l, p_r))
                p_l, p_r = c_l, c_r
        ivals.append((p_l, p_r))
        return ivals
