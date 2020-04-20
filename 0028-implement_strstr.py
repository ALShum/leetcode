class Solution:
    ## Manual
    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        scan_pos = 0
        while scan_pos < len(haystack):
            if haystack[scan_pos] == needle[0]:
                n = len(needle)
                if (scan_pos + n - 1) < len(haystack):
                    if haystack[scan_pos:scan_pos + n] == needle:
                        return scan_pos
                else:
                    break
            scan_pos += 1
        return -1

    ## Using python string method
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
