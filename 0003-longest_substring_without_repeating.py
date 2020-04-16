## Add letters seen so far into an array
## For each new letter check if seen before
## If seen before, restart array right after index of the letter seen before
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
