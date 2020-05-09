# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def bin_search(start,end):
            if start >= end:
                return start
            mid = (start+end)//2
            if not isBadVersion(mid):
                return bin_search(mid+1,end)
            else:
                return bin_search(start,mid)
            return -1
        return bin_search(1,n)
        """
        :type n: int
        :rtype: int
        """
        