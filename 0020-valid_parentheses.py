## use a stack

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        match = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in ('(', '{', '['):
                st.append(c)
            else:
                other = match.get(c)
                if len(st) > 0 and st[-1] == other:
                    st.pop()
                else:
                    return False
        return len(st) == 0
