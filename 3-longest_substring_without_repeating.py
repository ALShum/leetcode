class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_l = []
        max_l = 0

        for ss in s:
            if ss in str_l:
                str_l = str_l[str_l.index(ss) + 1:]
            str_l.append(ss)
            max_l = max(max_l, len(str_l))
        return max_l
