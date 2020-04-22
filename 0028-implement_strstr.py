class Solution:
    # For loop and then forward scan
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n = len(needle)
        for scan_pos in range(0, len(haystack)):
            if haystack[scan_pos] == needle[0]:
                if (scan_pos + n - 1) < len(haystack):
                    if haystack[scan_pos:scan_pos + n] == needle:
                        return scan_pos
                else:
                    break
        return -1

    # Cheat with python str methods
    def strStr2(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
