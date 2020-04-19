# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        badVer = {}
        def firstBadVersionInner(l, h):
            if l < h:
                m = (l + h) // 2
                badVer[m] = isBadVersion(m)

                # found a bad version
                if badVer[m]:
                    # if previous ver is good, then we found the first bad ver
                    if not badVer.get(m - 1, isBadVersion(m - 1)):
                        return m
                    return firstBadVersionInner(l, m)

                # found a good version
                else:
                    # if the next ver is bad, then we found the first bad ver
                    if badVer.get(m + 1, isBadVersion(m + 1)):
                        return m + 1
                    return firstBadVersionInner(m, h)
            return None

        return firstBadVersionInner(0, n)
